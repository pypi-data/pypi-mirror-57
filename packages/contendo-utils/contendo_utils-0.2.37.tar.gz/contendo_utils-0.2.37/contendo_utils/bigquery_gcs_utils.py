import logging

from google.cloud import bigquery
from google.cloud import storage
from gcsfs import GCSFileSystem
from google.api_core.exceptions import BadRequest

from .contendo_logging import *
from .ProUtils import ProUtils

class BigqueryUtils:
    def __init__(self, project=None):
        if project:
            self.__bigquery_client = bigquery.Client(project=project)
            self.__storage_client  = storage.Client(project=project)
        else:
            self.__bigquery_client = bigquery.Client()
            self.__storage_client  = storage.Client()

    def create_dataset(self, datasetId: str):
        #
        # Make sure the target dataset exists, or create it.
        try:
            assert datasetId in [dataset.dataset_id
                                  for dataset in list(self.__bigquery_client.list_datasets())]
        except AssertionError:  # dataset doesn't exist
            datasetReference = self.__bigquery_client.dataset(datasetId)
            dataset = bigquery.Dataset(datasetReference)
            dataset.location = 'US'
            dataset = self.__bigquery_client.create_dataset(dataset)

        return

    def upload_string_to_gcp(self, data, bucketName, targetFileName):
        bucket = self.__storage_client.get_bucket(bucketName)
        blob = bucket.blob(targetFileName)
        res = blob.upload_from_string(data)
        return 'gs://{}/{}'.format(bucketName, targetFileName)

    def read_string_from_gcp(self, bucketName, fromFileName):
        data = None
        try:
            bucket = self.__storage_client.get_bucket(bucketName)
            blob = bucket.blob(fromFileName)
            data = blob.download_as_string()
        #except storage. NotFound as e:
        #    print('Info: File not found in BigqueryUtils.read_string_from_gcp({}, {})', bucketName, fromFileName)
        except Exception as e:
            print ('Error in BigqueryUtils.read_string_from_gcp({}, {}) {}, trace {}', bucketName, fromFileName, e, type(e))

        return data

    def upload_file_to_gcp(self, bucketName, inFileName, targerFileName, timestamp=False):
        if timestamp:
            ts = str(os.path.getctime(inFileName))
            self.upload_string_to_gcp(data=ts, bucketName=bucketName, targetFileName=targerFileName+'.timestamp')
        bucket = self.__storage_client.get_bucket(bucketName)
        blob = bucket.blob(targerFileName)
        res = blob.upload_from_filename(inFileName)
        return 'gs://{}/{}'.format(bucketName, targerFileName)

    def download_from_gcp(self, bucketName, fromFileName, toFileName, checkTimestamp=False):
        try:
            bucket = self.__storage_client.get_bucket(bucketName)
            blob = bucket.blob(fromFileName)
            if os.path.exists(toFileName) and checkTimestamp:
                try:
                    ts = self.read_string_from_gcp(bucketName=bucketName, fromFileName=fromFileName+'.timestamp')
                    if float(ts)<=os.path.getctime(toFileName):
                        return False
                except Exception as e:
                    print('File not exists %s', fromFileName+'.timestamp')

            ProUtils.create_path_directories(toFileName)
            data = blob.download_to_filename(toFileName)
        #except storage. NotFound as e:
        #    print('Info: File not found in BigqueryUtils.read_string_from_gcp({}, {})', bucketName, fromFileName)
        except Exception as e:
            print ('Error in BigqueryUtils.read_string_from_gcp({}, {}) {}, trace {}', bucketName, fromFileName, e, type(e))
            raise e

        return True

    @contendo_classfunction_logger
    def create_table_from_gcp_file(
            self,
            gcpFileURI,
            datasetId,
            tableId,
            writeDisposition='WRITE_APPEND',
            fileType=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
            max_bad_records=0
    ):
        datasetRef = self.__bigquery_client.dataset(datasetId)
        job_config = bigquery.LoadJobConfig()
        job_config.autodetect = True
        job_config.max_bad_records=max_bad_records,
        job_config.write_disposition = writeDisposition
        job_config.source_format = fileType
        load_job = self.__bigquery_client.load_table_from_uri(
            gcpFileURI,
            datasetRef.table(tableId),
            job_config=job_config
        )
        try:
            result = load_job.result()
            if load_job.errors and len(load_job.errors)>0:
                logger.error('Error occured while loading file %s, errors: \n%s', gcpFileURI, load_job.errors)
        except BadRequest as be:
            logger.error('Error loading file %s, errors: %s', gcpFileURI, load_job.errors)
            raise be

        return result

    @contendo_classfunction_logger
    def create_table_from_local_file(self, localFile, datasetId, tableId, writeDisposition='WRITE_TRUNCATE', fileType=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON, schema=None):
        datasetRef = self.__bigquery_client.dataset(datasetId)
        job_config = bigquery.LoadJobConfig()
        job_config.autodetect = True
        job_config.write_disposition = writeDisposition
        job_config.source_format = fileType
        #job_config.max_bad_records = 100
        if schema and False:
            tableSchema = []
            for field in schema:
                tableSchema.append(bigquery.schema.SchemaField.from_api_repr(field))
            job_config.schema = tableSchema
        fileObj = open(localFile, 'rb')
        load_job = self.__bigquery_client.load_table_from_file(
            fileObj,
            datasetRef.table(tableId),
            job_config=job_config,
        )
        fileObj.close()

        try:
            result = load_job.result()
            if load_job.errors and len(load_job.errors)>0:
                logger.error('Error occured while loading file %s, errors: \n%s', localFile, load_job.errors)
        except BadRequest as be:
            logger.error('Error loading file %s, errors: %s', localFile, load_job.errors)
            raise be

        return result

    def get_table_schema(self, datasetId, tableId):

        datasetRef = self.__bigquery_client.dataset(datasetId)
        tableRef = datasetRef.table(tableId)
        table = self.__bigquery_client.get_table(tableRef)  # API Request

        schema = []
        for schemaField in table.schema:
            schema.append(schemaField.to_api_repr())

        return schema

    def execute_query(self, query):
        query_job = self.__bigquery_client.query(query)
        result = query_job.result()
        return result

    def execute_query_to_df(self, query, fillna=''):
        query_job = self.__bigquery_client.query(query)
        ret_df = query_job.result().to_dataframe().fillna(fillna)
        return ret_df

    def execute_query_to_dict(self, query, fillna=''):
        query_job = self.__bigquery_client.query(query)
        ret_df = query_job.result().to_dataframe().fillna(fillna)
        retDict = {}
        retDict['nRows'] = ret_df.shape[0]
        retDict['Columns'] = list(ret_df.columns)
        rows = []
        for i,row in ret_df.iterrows():
            rows.append(dict(row))
        retDict['Rows'] = rows
        return retDict

    def execute_query_with_schema_and_target(self, query, targetDataset, targetTable, schemaDataset=None, schemaTable=None):

        #
        # Reset the table based on schema
        writeDisposition = 'WRITE_TRUNCATE'
        if schemaDataset is not None and schemaTable is not None:
            copyJobConfig = bigquery.CopyJobConfig()
            copyJobConfig.write_disposition = 'WRITE_TRUNCATE'
            copy_job = self.__bigquery_client.copy_table(
                self.__bigquery_client.dataset(schemaDataset).table(schemaTable),
                self.__bigquery_client.dataset(targetDataset).table(targetTable),
                job_config=copyJobConfig
            )
            writeDisposition = 'WRITE_APPEND'

        #
        # Set job configuration & execute
        job_config = bigquery.QueryJobConfig()
        job_config.destination = self.__bigquery_client.dataset(targetDataset).table(targetTable)
        job_config.write_disposition = writeDisposition
        metrics_query_job = self.__bigquery_client.query(query, job_config=job_config)
        nRows = metrics_query_job.result().total_rows
        return nRows

    #def write_dataset_to_bigquery(self, pdDataset, targetTableId):


#import os
#os.chdir('~/PycharmProjects')
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="../sportsight-tests.json"
#bqu = BigqueryUtils()
#bqu.execute_query_with_schema_and_target('SELECT lastUpdatedOn  FROM `sportsight-tests.Baseball1.pbp_playoffs_2018` LIMIT 100', 'test_dataset', 'test_table')
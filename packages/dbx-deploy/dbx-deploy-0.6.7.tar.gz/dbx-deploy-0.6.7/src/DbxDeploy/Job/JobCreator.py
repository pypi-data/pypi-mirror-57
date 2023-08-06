from pathlib import PurePosixPath
from DbxDeploy.Setup.Version.VersionInterface import VersionInterface
from databricks_api import DatabricksAPI
from logging import Logger

class JobCreator:

    def __init__(
        self,
        clusterId: str,
        dbxProjectRoot: str,
        logger: Logger,
        dbxApi: DatabricksAPI
    ):
        self.__clusterId = clusterId
        self.__dbxProjectRoot = PurePosixPath(dbxProjectRoot)
        self.__logger = logger
        self.__dbxApi = dbxApi

    def create(self, notebookPath: PurePosixPath, version: VersionInterface):
        notebookReleasePath = version.getDbxVersionPath(self.__dbxProjectRoot).joinpath(notebookPath)

        self.__logger.info('Creating job for {}'.format(str(notebookReleasePath)))

        job = self.__dbxApi.jobs.create_job(
            name=str(notebookPath),
            existing_cluster_id=self.__clusterId,
            max_retries=-1,
            min_retry_interval_millis=30*1000,
            retry_on_timeout=True,
            notebook_task=dict(
                notebook_path=str(notebookReleasePath)
            ),
            max_concurrent_runs=1
        )

        self.__logger.info('Job #{} created'.format(job['job_id']))

        job['notebook_release_path'] = notebookReleasePath

        return job

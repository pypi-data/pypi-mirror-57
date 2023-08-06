import logging
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow_xplenty.client_factory import ClientFactory


class XplentyFindOrStartClusterOperator(BaseOperator):
    """Operator to find or start and Xplenty cluster

    Spin-up or re-use a cluster in the given environment ('sandbox' or
    'production')
    """

    TERMINATING_STATUSES = ["pending_terminate", "terminating", "terminated", "error"]

    @apply_defaults
    def __init__(
        self,
        env="sandbox",
        num_nodes=1,
        terminate_on_idle=False,
        time_to_idle=3600,
        **kwargs
    ):
        self.env = env
        self.num_nodes = num_nodes
        self.terminate_on_idle = terminate_on_idle
        self.time_to_idle = time_to_idle
        self.client = ClientFactory().client()

        super(XplentyFindOrStartClusterOperator, self).__init__(**kwargs)

    def execute(self, context):
        cluster = self.__find()
        if cluster is None:
            cluster = self.__start()
            logging.info(
                "Starting new Xplenty %s cluster with id %d.", self.env, cluster.id
            )

        return cluster.id

    def __find(self):
        offset = 0
        page_size = 100
        while True:
            clusters = self.client.get_clusters(offset=offset, limit=page_size)
            if not clusters:
                return None

            for cluster in clusters:
                if self.__is_useable(cluster):
                    logging.info(
                        "Found existing Xplenty %s cluster with id %d.",
                        self.env,
                        cluster.id,
                    )
                    return cluster

            offset += page_size

    def __start(self):
        return self.client.create_cluster(
            self.env,
            self.num_nodes,
            "airflow-%s-cluster" % self.env,
            "Cluster to run Airflow packages",
            terminate_on_idle=self.terminate_on_idle,
            time_to_idle=self.time_to_idle,
        )

    def __is_useable(self, cluster):
        if cluster.type != self.env:
            return False
        elif cluster.status in self.TERMINATING_STATUSES:
            return False

        return True

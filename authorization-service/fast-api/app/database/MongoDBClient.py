import motor.motor_tornado
from shared.env_var_utility import *
from shared.singleton_decorator import singleton_decorator


@singleton_decorator
class MongoDBClient:
    def __init__(self):
        self.__client = None

        self.__mongo_host = get_environment_variable("MONGO_HOST")
        self.__mongo_port = get_environment_variable("MONGO_PORT")
        self.__mongo_username = get_environment_variable("MONGO_INITDB_ROOT_USERNAME")
        self.__mongo_password = get_environment_variable("MONGO_INITDB_ROOT_PASSWORD")

        mongodb_uri = "mongodb://{}:{}@{}:{}".format(self.__mongo_username, self.__mongo_password,
                                                     self.__mongo_host, self.__mongo_port)
        print("Mongo client sets to connect at {}".format(mongodb_uri))
        self.__client = motor.MotorClient(mongodb_uri,
                                          serverSelectionTimeoutMS=5000)

    async def get_database(self, database_name: str) -> motor.MotorDatabase:
        return self.__client[database_name]

    async def list_collection_names(self, database_object: motor.MotorDatabase) -> list[str]:
        return await database_object.list_collection_names()

    async def get_collection(self, database_object: motor.MotorDatabase, collection_name: str) -> motor.MotorCollection:
        return database_object[collection_name]

import boto3


class DistributedFileSystem:
    def __init__(self):
        self.client = boto3.client('s3')

    def read_file(self, path: str) -> bytes:
        data = self.client.get_object(Key=path)
        return data['Body'].read()

    def write_file(self, path: str, file: bytes):
        self.client.put_object(Body=file, Key=path)


from abc import ABC, abstractmethod

# import boto3


# class DistributedFileSystem(ABC):
#     @abstractmethod
#     def read_file(path: str) -> bytes:
#         pass

#     @abstractmethod
#     def write_file(path: str, file: bytes):
#         pass


# class BotoS3Client(DistributedFileSystem):
#     def __init__(self):
#         self.client = boto3.client('s3')

#     def read_file(path: str) -> bytes:
#         data = self.client.get_object(Key=path)
#         return data['Body'].read()

#     def write_file(path: str, file: bytes):
#         self.client.put_object(Body=file, Key=path)


# class HDFSClient(DistributedFileSystem): ...
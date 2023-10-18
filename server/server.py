import image_pb2_grpc as image_grpc
import image_pb2
import os
import grpc
from concurrent import futures
import random

IMAGE_DIRECTORY = os.getcwd() + '/database'
print(IMAGE_DIRECTORY)

class ImageSearch(image_grpc.ImageSearchServicer):
    
    def searchImage(self, request, context):
        keyword = request.keyword
        image_path = self.get_random_image(keyword)

        if image_path:
            with open(image_path, 'rb') as image_file:
                image_data = image_file.read()
                return image_pb2.ImageResponse(image=image_data)
        else:
            context.set_details(f"No images found for keyword: {keyword}")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return image_pb2.ImageResponse()


    def get_random_image(self, keyword):
        object_class_dir = os.path.join(IMAGE_DIRECTORY, keyword)
        print(object_class_dir)
        print(os.path.exists(object_class_dir))

        if os.path.exists(object_class_dir):
            images = os.listdir(object_class_dir)
            if images:
                random_image = random.choice(images)
                image_path = os.path.join(object_class_dir, random_image)
                return image_path

        return None
    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_grpc.add_ImageSearchServicer_to_server(ImageSearch(), server)
    server.add_insecure_port('localhost:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
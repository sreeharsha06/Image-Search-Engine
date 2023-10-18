import grpc
import image_pb2 as image_pb2
import image_pb2_grpc as image_grpc
import os


IMAGE_DIRECTORY = os.getcwd() + '/output'

def run_client():
    channel = grpc.insecure_channel('localhost:50051')

    client = image_grpc.ImageSearchStub(channel)

    try:
        keyword = "dogs"
        request = image_pb2.ImageRequest(keyword=keyword)
        response = client.searchImage(request)

        if response.image:
            save_image(response.image, f"{keyword}.jpg")
        else:
            print("No image found for the keyword:", keyword)

    except grpc.RpcError as e:
        print(f"Error: {e.details()}")

def save_image(image_data, filename):
    # Save the received image data to a file
    if not os.path.exists(IMAGE_DIRECTORY):
        os.mkdir(IMAGE_DIRECTORY)
    with open(os.path.join(IMAGE_DIRECTORY, filename), 'wb') as image_file:
        image_file.write(image_data)

if __name__ == '__main__':
    run_client()

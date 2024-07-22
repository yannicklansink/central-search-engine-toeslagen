using Azure.Identity;
using Azure.Storage.Blobs;
using System.Threading.Tasks;

namespace WebApp.Components.Services
{
    public class BlobService
    {
        private readonly BlobContainerClient _blobContainerClient;

        public BlobService()
        {
            var blobServiceClient = new BlobServiceClient(
                new Uri("https://bestandenstorage.blob.core.windows.net"),
                new DefaultAzureCredential());

            _blobContainerClient = blobServiceClient.GetBlobContainerClient("bestandentrigger");
        }

        public async Task UploadFromFileAsync(string localFilePath, string originalFileName)
        {
            // Controleer of de container bestaat en maak deze aan indien nodig
            await _blobContainerClient.CreateIfNotExistsAsync();

            BlobClient blobClient = _blobContainerClient.GetBlobClient(originalFileName);

            await blobClient.UploadAsync(localFilePath, true);
        }
    }
}

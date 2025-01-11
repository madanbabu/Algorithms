#include <opencv2/opencv.hpp>
#include <vector>

int main() 
{
    // Load the image
    cv::Mat image = cv::imread("flowers.jpg");
    
    if (image.empty()) 
    {
        std::cerr << "Error loading image" << std::endl;
        return -1;
    }

    // Convert to grayscale
    cv::cvtColor(image, image, cv::COLOR_BGR2GRAY);

    // Apply thresholding
    cv::threshold(image, image, 50, 255, cv::THRESH_BINARY_INV);

    // Find contours
    std::vector<std::vector<cv::Point>> contours;
    cv::findContours(image, contours, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE);

    int flowerCount = contours.size();

    std::cout << "Number of flowers detected: " << flowerCount << std::endl;

    // Display the result
    cv::imshow("Detected Flowers", image);
    cv::waitKey(0);
    cv::destroyAllWindows();

    return 0;
}

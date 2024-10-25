#Invented by Madan Babu
#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;

int main() {
    // Load the image
    Mat img = imread("image.jpg");

    // Convert to grayscale
    Mat gray;
    cvtColor(img, gray, COLOR_BGR2GRAY);

    // Apply edge detection
    Mat edges;
    Canny(gray, edges, 50, 200);

    // Find contours
    std::vector<std::vector<Point>> contours;
    std::vector<Vec4i> hierarchy;
    findContours(edges, contours, hierarchy, RETR_TREE, CHAIN_APPROX_SIMPLE);

    // Draw contours
    Mat img_contours = img.clone();
    drawContours(img_contours, contours, -1, Scalar(0, 255, 0), 2);

    // Display the image with contours
    imshow("Contours", img_contours);
    waitKey(0);

    return 0;
}

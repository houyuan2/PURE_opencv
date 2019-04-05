// CPP program to Stitch 
// input images (panorama) using OpenCV  
#include <iostream> 
#include <fstream> 
  
// Include header files from OpenCV directory 
// required to stitch images. 
#include "opencv2/imgcodecs.hpp" 
#include "opencv2/highgui.hpp" 
#include "opencv2/stitching.hpp" 
  
using namespace std; 
using namespace cv; 
  
// Define mode for stitching as panoroma  
// (One out of many functions of Stitcher) 
Stitcher::Mode mode = Stitcher::PANORAMA; 
  
// Array for pictures 
vector<Mat> imgs; 
  
int main(int argc, char* argv[]) 
{ 
    // Get all the images that need to be  
    // stitched as arguments from command line  
    // for (int i = 1; i < argc; ++i) 
    // { 
    //         // Read the ith argument or image  
    //         // and push into the image array 
    //         Mat img = imread(argv[i]); 
    //         if (img.empty()) 
    //         { 
    //             // Exit if image is not present 
    //             cout << "Can't read image '" << argv[i] << "'\n"; 
    //             return -1; 
    //         } 
    //         imgs.push_back(img); 
    // } 

    string folder_path = "";
    string result_name = "";
    for (int i = 1; i < argc; ++i) {
        if (string(argv[i]) == "-s")
        {
            folder_path = argv[i + 1];
            i++;
        }

        if (string(argv[i]) == "-out")
        {
            result_name = argv[i + 1];
            i++;
        }
    }

    if (folder_path != "") {
        folder_path = folder_path + "/*.jpg";
    } else {
        folder_path = "images/*.jpg"
    }
    cv::String path(folder_path); //select only jpg
    vector<cv::String> fn;
    vector<cv::Mat> data;
    cv::glob(path,fn,true); // recurse
    for (size_t k=0; k<fn.size(); ++k)
    {
        cv::Mat im = cv::imread(fn[k]);
        if (im.empty()) continue; //only proceed if sucsessful
        // you probably want to do some preprocessing
        data.push_back(im);
    }

    imgs = data;

    // Define object to store the stitched image 
    Mat pano; 
      
    // Create a Stitcher class object with mode panoroma 
    Ptr<Stitcher> stitcher = Stitcher::create(mode); 
      
    // Command to stitch all the images present in the image array 
    Stitcher::Status status = stitcher->stitch(imgs, pano); 
  
    if (status != Stitcher::OK) 
    { 
        // Check if images could not be stiched 
        // status is OK if images are stiched successfully 
        // cout << "Can't stitch images\n"; 
        cout << "Can't stitch images, error code = " << int(status) << endl;
        return -1; 
    } 
      
    // Store a new image stiched from the given  
    //set of images as "result.jpg" 
    if (result_name == "") {
        result_name = "result.jpg";
    }
    imwrite(result_name, pano); 
      
    // Show the result 
    imshow("Result", pano); 
      
    waitKey(0); 
    return 0; 
}
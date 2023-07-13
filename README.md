# skincare-recommender-system
![image-2](https://github.com/billymwangi/skincare-recommender-system/assets/124556898/24228950-4f11-4adb-8f1e-6003ceef503a)


## Introduction 
This repository contains code and resources for a skincare recommender system project. The primary objective of this project is to analyze skincare data and provide personalized recommendations to users.

## Table of contents 
- [Installation](##Installation)
- [Data](##Data)
- [Modeling](##Modeling)
- [Evaluation](#Evaluation)
- [Deployment](##Model-Deployment)
- [Conclusion](#Conclusion)
- [Recommendations](#Recommendations)
- [Next Steps](#Next-Steps)
- [Challenges](#Challenges)
- [Collaborators](##Collaborators)

- ## Installation
- To set up the skincare recommender system project, follow the steps below:

- 1. Clone this repository :
     git clone [git@github.com:billymwangi/skincare-recommender-system.git](https://github.com/billymwangi/skincare-recommender-system)

      Alternatively, you can download the repository as a ZIP file and extract it to your local machine.

  2. Navigate to the project directory:
     
     cd skincare-recommender

  3. Create a virtual environment (optional)

     python3 -m venv env
     
     source env/bin/activate   # For Linux/Mac
     
     env\Scripts\activate      # For Windows

  5. Install the required dependencies:
     pip install -r requirements.txt

     Once the installation steps are complete, you are ready to proceed with using the skincare recommender system.

     Note: We recommend you  use Python 3.8 and above for this repository

  ## Data
  We scraped our data from the Sephora website using Apify and merged it with another dataset obtained from Kaggle.
  The dataset contains :

  * information about all beauty products (over 8,000) from the Sephora online store, including product and brand names, prices, ingredients, ratings, and all features.
  * user reviews (over 1 million on over 2,000 products) of all products from the Skincare category, including user appearances, and review ratings by other users

 The most helpful products visualization
 ![image](https://github.com/billymwangi/skincare-recommender-system/assets/124556898/20ba12a5-1082-4027-a334-c390d7a07181)


 ## Modeling
 The following models were developed:
 
 **Memory-Based Collaborative Filtering**

* **Model 1: Nearest Neighbors Model**: This model utilizes a Nearest Neighbors algorithm to find similar skincare profiles and make recommendations based on their preferences. The Nearest Neighbors algorithm calculates the similarity between a given user's skincare profile and other profiles in the dataset and then recommends products that have been positively rated by similar users.

* **Model 2: KNNBasic Model**: This  utilizes a K-Nearest Neighbors algorithm to find similar skincare profiles and make recommendations based on their preferences.
 
 **User-Based Collaborative Filtering**
 
* **Model 3: SVD Model**: The Singular Value Decomposition (SVD) model captures underlying relationships and generates recommendations based on these latent features.

* **Model 4: SVDpp Model**: Building upon the SVD model, the SVD++ algorithm further considers implicit feedback signals, such as user interactions and implicit preferences, to enhance the recommendation process. This model incorporates additional user information such as skin color, hair color, skin type, and skin tone for more accurate and personalized skincare recommendations.


  ## Evaluation

The performance of the models was evaluated using root mean square error (RMSE), Mean Absolute Error(MAE), Precision, recall, and accuracy of higher than 90. The following are the RMSE values obtained for each model:

- KNNBasic model: RMSE = 0.2724, MAE = 0.2132, Precision = 0.999 ,Recall=1.0, Accuracy = 0.999
- SVD model: RMSE = 0.0343, MAE =0.0158, Precision = 0.9999 ,Recall=1.0, Accuracy = 0.9998
- SVDpp model: RMSE =  0.0290 , MAE =0.0113  , Precision = 0.9997 ,Recall=1.0, Accuracy = 0.9997
- Tuned SVDpp model: RMSE = 0.0283, MAE = 0.0099, Precision = 0.9998 ,Recall=1.0, Accuracy = 0.9998

These RMSE values provide insights into the accuracy of the models in predicting skincare preferences and their effectiveness in generating recommendations.

   
## Model-Deployment

Our model was deployed using Streamlit, a Python framework for building web applications. We created a user-friendly interface where users can input their budget (in dollars), skin tone, skin type, and the type of product they are looking for. The deployed system then generates personalized skincare recommendations based on these inputs.

The interface presents the following information for each recommended product:

- Product Name: The name of the recommended skincare product.
- Brand: The brand associated with the recommended product.
- Ingredients: The list of ingredients used in the recommended product.
- Average Rating: The average rating or review score for the recommended product.

By considering user preferences and utilizing the trained models, the system provides tailored recommendations that align with the user's budget, skin tone, skin type, and desired product type.

  ## Conclusions

In this skincare recommender system project, we developed several models to provide personalized skincare recommendations to users. We utilized memory-based collaborative filtering models, such as the Nearest Neighbors and KNNBasic models, as well as user-based collaborative filtering models, such as the SVD and SVDpp models.

The Tuned SVDpp model, after tuning, achieved the best results with high precision, recall, and accuracy scores demonstrating its ability to provide the most accurate recommendations.

We were able to generate personalized skincare recommendations based on their budget, skin tone, and skin type.

Overall, this project successfully demonstrates the effectiveness of collaborative filtering techniques in generating tailored skincare recommendations. By leveraging user preferences and product information, we enable users to discover skincare products that align with their needs and preferences.

The skincare recommender system has the potential to enhance the user experience, simplify product selection, and facilitate informed decision-making in the realm of skincare. We hope that this project serves as a useful tool for skincare enthusiasts and helps them find the most suitable products for their skincare routine.



  ## Reccommendations

Based on our experience in developing the skincare recommender system, we would like to provide the following recommendations:

1. The business should provide more products such as face serums since they were rated as the most helpful.
   
2. They should collect more reviews from all races to improve the accuracy of the recommendation system.

3. They should Collaborate with skincare experts, dermatologists, or industry professionals who can provide valuable 
  insights and expertise on the quality and safety of skincare products.

5. Alongside the product recommendations, the business can provide educational resources such as skincare guides, tutorials, and tips. This can help users make informed decisions about their skincare routines, understand the benefits of different ingredients, and address specific skin concerns
 

## Next-Steps
 

While the skincare recommender system project has achieved promising results, there are several potential next steps to consider for further improvements and enhancements:

1. Incorporate natural language processing (NLP).
   
2. Explore deep learning models.

3. Integrate external data sources: Explore the integration of external data sources, such as social media platforms, beauty blogs, or skincare forums, to gather additional user-generated content and insights. 

4. Collaborate with skincare brands and retailers.

5. Conduct A/B testing and user studies: Perform rigorous A/B testing to evaluate the performance of different recommendation algorithms or strategies.

By pursuing these next steps, the skincare recommender system can evolve into a more advanced and sophisticated tool that provides users with highly personalized skincare recommendations and an enhanced user experience.



  ## Challenges
   Lack of data for dark skin tones: One specific challenge we encountered was the limited availability of data for individuals with dark skin tones. Skincare recommendations need to consider different skin tones and address specific concerns related to dark skin. Collecting more diverse data and ensuring the representation of all skin tones would be beneficial for providing accurate recommendations to a wider range of users.


  ## Collaborators 
-[Cynthiah Mulwo](https://github.com/Cynthiah-Mulwo)

-[Brian Nderu](https://github.com/BrianNderu)

-[Paul Musau](https://github.com/PaulMawa)

-[Priscilla Kamiri](https://guthub.com/waihiga9)

-[Kellen Kinya](https://github.com/kellenkinya)

-[Billy Mwangi](https://github.com/billymwangi)
    


    
     

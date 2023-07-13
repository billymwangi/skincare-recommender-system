# skincare-recommender-system

## Introduction 
This repository contains code and resources for a skincare recommender system project. The primary objective of this project is to analyze skincare data and provide personalized recommendations to users. By exploring various skincare patterns and gaining insights into different skincare products, this system aims to assist individuals in achieving healthier and more vibrant skin.

## Table of contents 
- [Business Overview](#business-overview)
- [Installation](#installation)
- [Data](#data)
- [Modeling](#modeling)
- [Evaluation](#evaluation)
- [Conclusion](#conclusion)
- [Recommendations](#recommendations)
- [Next Steps](#nextsteps)
- [Contributing](#contributing)
- [License](#license)

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

  4. Install the required dependencies:
     pip install -r requirements.txt

     Once the installation steps are complete, you are ready to proceed with using the skincare recommender system.

     Note: We recommend you  to use Python 3.9 and above for this repository

  ## Data
  We scraped our data from the Sephora website using Apify and merged it with another dataset obtained from Kaggle .
  The dataset contains :

  * information about all beauty products (over 8,000) from the Sephora online store, including product and brand names, prices, ingredients, ratings, and all features.
  * user reviews (over 1 million on over 2,000 products) of all products from the Skincare category, including user appearances, and review ratings by other users
     

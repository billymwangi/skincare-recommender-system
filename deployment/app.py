import streamlit as st
import pandas as pd
from surprise import SVD
import pickle




# Add your Streamlit app content below

# Load the SVD++ model
with open('svdpp_model.pkl', 'rb') as f:
    model = pickle.load(f)

new_data = pd.read_csv('new-data.csv', low_memory= False)


# Engineer the price_range column
def engineer_price_range(price):
    if price < 32:
        return 'low'
    elif price < 68:
        return 'medium'
    else:
        return 'high'

new_data['price_range'] = new_data['price_usd_x'].apply(engineer_price_range)


def generate_recommendation(price_range, tertiary_category, skin_type, skin_tone,model):
    # Filter products based on user input criteria
    filtered_data = new_data[
        (new_data['price_range'] == price_range) &
        (new_data['tertiary_category'] == tertiary_category) &
        (new_data['skin_type'] == skin_type) &
        (new_data['skin_tone'] == skin_tone)
    ]
   # Select a random product from the filtered data
    if not filtered_data.empty:
        sorted_data = filtered_data.sort_values(by='rating_x', ascending=False)
        product_id = sorted_data['product_id'].iloc[0]
        # Generate prediction for the selected product
        prediction = model.predict('new_user', product_id)

        # Return product name and ingredients
        product_name = sorted_data['product_name_x'].iloc[0]
        ingredients = sorted_data['ingredients'].iloc[0]
        brand_name = sorted_data['brand_name_x'].iloc[0]
        price = sorted_data['price_usd_x'].iloc[0]
        highlights = sorted_data['highlights'].iloc[0]
        return product_name, ingredients, prediction, brand_name, price, highlights
    return None, None

# Define the input form
st.header('Skin Care Product Recommendation')

with st.form(key='skin_care_recommendation_form'):
    tertiary_category = st.selectbox('Select Product Category', ('Blemish & Acne Treatments', 'Eye Creams & Treatments', 'Exfoliators', 'Face Masks', 'Face Oils', 'Face Serums', 'Face Sunscreen', 'Face Wash & Cleansers', 'Facial Peels', 'Makeup Removers', 'Mist & Essences', 'Moisturizers', 'Toners'))
    skin_type = st.selectbox('Select Skin Type', ('combination', 'dry','normal', 'oily'))
    skin_tone = st.selectbox('Select Skin Tone', ('fair','light','medium','tan'))
    price_input = st.number_input('Enter your Budget in KSH', min_value=420.00, max_value=59500.00, step=1.00)
    price_result = price_input/140
    price_range= engineer_price_range(price_result)
    submit_button = st.form_submit_button(label='Generate Recommendations')

if submit_button:
    product_name, ingredients, prediction, brand_name, price, highlights = generate_recommendation(price_range, tertiary_category, skin_type, skin_tone,model)
    if product_name and ingredients and prediction and brand_name and price and highlights:
        st.success('**Recommended Product:**')
        st.write('**Product Name:**',f'<span style="font-size: 20px;"><b>{product_name}</b></span>', unsafe_allow_html=True)
        st.write('**Brand Name:**', f'<span style="font-size: 20px;"><b>{brand_name}</b></span>', unsafe_allow_html=True)
        st.write('**Price in KSH:**', f'<span style="font-size: 20px;"><b>{price * 140}</b></span>', unsafe_allow_html=True)
        rating = round(prediction.est, 2)
        stars = int(rating)
        star_symbols = '★' * stars
        st.write('**Reviews Rating (out of 5):**', f'<span style="font-size: 20px;"><b>{rating} {star_symbols}</b></span>', unsafe_allow_html=True)
        # st.write('**Review Rating:**', f'<span style="font-size: 20px;"><b>{round(prediction.est, 2)/5}</b></span>', unsafe_allow_html=True)
        st.write('**Product Highlights:**', highlights)
        st.write('**Ingredients:**', ingredients)

    else:
        st.warning('No product found matching the criteria.')
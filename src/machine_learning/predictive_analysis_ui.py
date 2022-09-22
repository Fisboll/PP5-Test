import streamlit as st

def predict_price(X_live, house_features, price_pipeline):

	# from live data, subset features related to this pipeline
	X_live_price = X_live.filter(house_features)

	# predict
	price_prediction = price_pipeline.predict(X_live_price)
	# st.write(tenure_prediction_proba)

	# create a logic to display the results
	
	statement = (
			f"* The price of a house with the given attribute values is: **{price_prediction[0]}**."
			f"* The features used are: **{X_live_price}**."
			)
	
	st.write(statement)


def predict_inheritted_house_price(X_inheritted, house_features, price_pipeline):

	# From inheritted houses data, subset features related to this pipeline
	X_inheritted_price = X_inheritted.filter(house_features)

	# predict

	price_prediction_inheritted = price_pipeline.predict(X_inheritted_price)
	# st.write(tenure_prediction_proba)
	
	this_price = price_prediction_inheritted[0]
	# create a logic to display the results
	
	statement = (
			f"* Price of this house: **{price_prediction_inheritted[0]}**.\n"
			)
	
	st.write(statement)
	return this_price
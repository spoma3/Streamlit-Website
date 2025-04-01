import streamlit as st
import pandas as pd
st.set_page_config(page_title = "CS 4641 Group #47 Team Proposal", page_icon = ":potted_plant:", layout = "wide")
# st.subheader("Want to watch our unlisted Youtube video on this topic go [here](https://youtu.be/Uc_2V9tAKqM)")
st.write("---")
# --- HEADER SECTION ----
with st.container():
    left_column, right_column = st.columns(2)
    with right_column:
        st.image("SoyBeanImage.jpg", width = 450, caption="Soybean Farm")
    with left_column:
        st.subheader("Introduction/Background")
        st.title("Literature Review")
        st.write("Our topic of choice is Advanced Soybean Agriculture, more specifically predicting soybean yield based on salicylic acid treatment, genotype, and water stress. Pre–existing research has found that salicylic acid treatments of 100-200 parts per million result in significantly higher soybean yields [1]. Furthermore, genotypes with larger roots systems tend to have water retention rates, which also results in higher yields [2]. Higher levels of water stress are often associated with lower plant height and weight, leaf size, and overall seed yield [3].")
        st.title("Dataset Description")
        st.write("Our dataset is “Advanced Soybean Agricultural Dataset” from Kaggle. This dataset consists of parameters including genotype, salicylic acid treatment, and water stress. There are 6 different genotypes, 3 levels of salicylic acid treatment: 250 mg, 450 mg, and 0 mg, and 2 levels of water stress: 5% and 70%. Furthermore, the dataset shows various quantitative metrics based on parameters such as plant height, biological weight, number of pods, and many others.")
        st.title("Dataset Link")
        st.write("[Dataset Link is here](https://www.kaggle.com/datasets/wisam1985/advanced-soybean-agricultural-dataset-2025)")
        st.subheader("Problem Definition")
        st.title("Problem")
        st.write("Using current agricultural practices, it is difficult to predict and optimize soybean yield and health. This leads to inconsistencies that can potentially cause supply chain disruptions, price instability, inefficient allocation of resources, and an overall decline in quality and output. With the soybean industry already fraught with supply chain bottlenecks, it is imperative to determine the most efficient method to yield the highest quantity and quality of soybeans in order to meet rising global demand.")
        st.subheader("Methods")
        st.title("Normalization of Data")
        st.write("The data preprocessing methods chosen for this project aim to enhance the accuracy of the machine learning algortihm while reducing the risk of overfitting. So far, normalization and z-score standardization have been implemented. Normalization was applied to prevent certain features from disproportionately influencing model weights and loss functions. This issue arises when some features have naturally larger values, amplifying the impact of incorrect estimates. Normalization was implemented with the following equation:  norm_val = (vals – min(val)) / (max(val) - min(val)).")
        st.image("Normalization Function.png")
        st.title("Random Forest Regression Model")
        st.write("Following normalization, a supervised learning Random Forest Regressor was developed. THis model was chosen because it is resistant to outliers and inherently reduces the influence of less important features. This makes it a valuable tool for assessing the potential accuracy of neural networks and Bayesian neural networks. Additionally, the Random Forest Regressor model generates a feature importance ranking, which helps identify any overreliance on specific features. The results indicate a strong dependence on ChlorophyllA663 with Genotype as a close second. This ranking will be useful in the upcoming Principal Component Analysis (PCA) to ensure that critical features are not mistakenly removed.")
        st.image("Feature Importance Graph.png")
        st.title("Outlier Removal")
        st.write("Zscore standardization (z_score()) was also applied with a threshold of three standard deviations to detect and remove outliers. This step prevents distortions in the loss function and gradients, safeguarding the neural network model from reduced accuracy due to extreme values affecting weights and biases.")
        st.image("Outlier Removal.png")
        st.title("Neural Network")
        st.write("Finally, a supervised learning Neural Network was implemented to capture complex variable interactions and improve predictive accuracy, setting the foundation for constructing the Bayesian Neural Network.")
        st.image("Neural Network.png")
        st.title("Visualization")
        st.write("We performed two experiments using different machine learning models to predict the seed yield per unit area (SYUA) based on a reduced feature set. Below are the visualizations representing the performance of the models.")
        st.title("Random Forest Regressor Model")
        st.write("We evaluated the Random Forest Regressor (RFR) model by varying the number of trees and observing the change in the R² error. The following graph shows how the R² error changed with the number of trees:")
        st.image("RFR_R^2.png")
        st.caption(f"Figure 1. As shown in the plot, the R² error levels out as the number of trees passes 100, indicating that increasing the number of trees past 100 doesn’t improve the model's performance.")
        st.title("Neural Network Model")
        st.write("The loss of the neural network model during training was visualized over epochs. The following graph shows the loss curve")
        st.image("NN_Loss.png")
        st.caption(f"Figure 2. This plot demonstrates that the model steadily decreased its loss over the 8 epochs, which indicates that the training process was effective and the model was able to learn meaningful patterns in the data.")
        st.title("Quantitative Metrics")
        st.title("Random Forest Regressor (RFR) Model")
        st.write("After selecting the optimal number of trees (410), we evaluated the Random Forest model on the test set, achieving an R² score of 0.9924. This indicates that the model can explain 99.24% of the variance in the seed yield per unit area. Such a high R² score suggests that the model has performed exceptionally well on the test data.")
        st.title("Neural Network Model")
        st.write("The neural network achieved a R² score of 0.9726, which is also a strong result, indicating the model is able to predict the seed yield with good accuracy. The mean squared error (MSE) for the model is 0.0013, suggesting the predictions are close to the actual values.")
        st.title("Analysis of Model Performance")
        st.title("Random Forest Regressor (RFR)")
        st.write("The RFR model performed very well, with a very high R² score. This suggests that the ensemble approach of Random Forest, using multiple decision trees, is well-suited to our problem. The model's performance could be attributed to its ability to model non-linear relationships and handle feature interactions. The feature importance could also be investigated further to see how each input feature contributes to the prediction.")
        st.title("Neural Network")
        st.write("The neural network's performance is also commendable, with an R² score of 0.9726. However, the model was trained over only 8 epochs, which may limit its ability to fully optimize and achieve better performance. A longer training period or additional hyperparameter tuning could potentially lead to improved results. One reason the neural network might have performed slightly worse than the Random Forest model is its sensitivity to hyperparameters such as learning rate, batch size, and epoch count. Further experimentation with these parameters could improve its performance.")
        st.title("Next Steps")
        st.title("Third Model: Bayesian Neural Network (BNN)")
        st.write("Next, we will implement a Bayesian Neural Network (BNN) using TensorFlow and TensorFlow Probability, incorporating probabilistic reasoning and uncertainty estimation. The model will use a Dense Variational layer to apply Bayesian inference to the weights, allowing for more robust predictions. We will train the BNN with the Adam optimizer, tracking both the typical regression loss and the KL divergence regularization to assess the impact of uncertainty in the model's predictions.")
        st.subheader("Contributions Table")
        st.image("Contributions_Table.png", width = 300, caption = "Contributions")
        st.subheader("Gantt Chart")
        st.image("Gantt_Chart.png", width = 2500, caption = "Gantt Chart")
        st.subheader("References")
        st.title("References")
        st.write("[1]P. Kuchlan and M.K. Kuchlan, “Effect of Salicylic Acid on Plant Physiological and Yield Traits of Soybean,” Legume Research - An International Journal, no. Of, Mar. 2021, doi: https://doi.org/10.18805/lr-4527.")
        st.write("[2]Nisarga Kodadinne Narayana, Chathurika Wijewardana, F. A. Alsajri, K. Raja Reddy, S. R. Stetina, and Raju Bheemanahalli, “Resilience of soybean genotypes to drought stress during the early vegetative stage,” Scientific Reports, vol. 14, no. 1, Jul. 2024, doi: https://doi.org/10.1038/s41598-024-67930-w.")
        st.write("[3]M. S. Hossain et al., “Differential Drought Responses of Soybean Genotypes in Relation to Photosynthesis and Growth-Yield Attributes,” Plants, vol. 13, no. 19, pp. 2765–2765, Oct. 2024, doi: https://doi.org/10.3390/plants13192765.")
        st.write("[4] S. Jaiswal, “What is normalization in machine learning? A comprehensive guide to data rescaling,” DataCamp, https://www.datacamp.com/tutorial/normalization-in-machine-learning (accessed Feb. 20, 2025).")
        st.write("[5] “Normalize,” scikit, https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.normalize.html (accessed Feb. 20, 2025).")
        st.write("[6] “Primary supervised learning algorithms used in Machine Learning: Exxact blog,” Exxact, https://www.exxactcorp.com/blog/Deep-Learning/primary-supervised-learning-algorithms-used-in-machine-learning (accessed Feb. 20, 2025).")
        st.write("[7] “Randomforestregressor,” scikit, https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html (accessed Feb. 20, 2025).")
        st.write("[8] “What is Random Forest?,” IBM, https://www.ibm.com/think/topics/random-forest (accessed Feb. 20, 2025).")
        st.write("[9] L. Hardester, “Explained: Neural networks,” MIT News | Massachusetts Institute of Technology, https://news.mit.edu/2017/explained-neural-networks-deep-learning-0414 (accessed Feb. 20, 2025).")
        st.write("[10] “4.2. permutation feature importance,” scikit, https://scikit-learn.org/stable/modules/permutation_importance.html (accessed Feb. 20, 2025).")
        st.write("[11] J. Q. Yu, E. Creager, D. Duvenaud, and J. Bettencourt, Bayesian Neural Networks, https://www.cs.toronto.edu/~duvenaud/distill_bayes_net/public/ (accessed Feb. 20, 2025).")
        st.write("[12] L. Sturlaugson, “Principal component analysis preprocessing with Bayesian networks ...,” Principal Component Analysis Preprocessing with Bayesian Networks for Battery Capacity Estimation, https://www.cs.montana.edu/sheppard/pubs/i2mtc-2013.pdf (accessed Feb. 21, 2025).")

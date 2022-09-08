![](./img/logo_small.png)
![](./img/derby.png)

## Mediterranean College | University of Derby
### MSc Big Data Analysis

<table>
    <tr>
        <th>Project</th>
        <td>Master Thesis</td>
    </tr>
    <tr>
        <th>Topic</th>
        <td><em>Data driven design of the next Google Play Store app</em></td>
    </tr>
    <tr>
        <th>Student</th>
        <td>Angelos Konioris</td>
    </tr>
    <tr>
        <th>Period</th>
        <td>Spring 2022</td>
    </tr>
</table>

Data Source: https://www.kaggle.com/datasets/gauthamp10/google-playstore-apps

Data description: This dataset contains Application data of more than 2.3 million applications with the following 24 attributes:

App Name, App Id, Category, Rating, Rating Count, Installs, Minimum Installs, Maximum Installs, Free, Price, Currency, Size,
Minimum Android, Developer Id, Developer Website, Developer Email, Released, Privacy Policy, Last Updated, Content Rating,
Ad Supported, In app purchases, Editor Choice, Scrapped Time

**Summary**

Nowadays, mobile phones and smartphones in particular are an integral part and tool in everyone’s life. They provide incredible capabilities through the Internet and applications, simplifying our lives in several ways. As a result, developers and companies invest their money and resources to create mobile applications fit for the existing operating systems. In this thesis, after the comparison of the two most popular mobile operating systems, iOS and Android, we decided to focus on the Google Play Store, which is the app store that Android devices have access to. The aim of this study is to propose a data driven design for a Google Play Store App based on the initial costs that are needed to create an application and to pro-vide satisfactory predictions about whether an app can be successful in terms of profit and downloads in the store market. Thus, we use a dataset of more than 2.3 million applications and 24 attributes that helps us with our analysis.

The first phase of our data was about the data loading in which we included all the steps regarding the importing of our dataset and some data cleansing tech-niques in which we kept only the top 10 categories based on the number of apps. Then, in the section of EDA, we created some plots split in univariate, bivariate and multivariate so we could have a deeper understanding of the distribution of our data and the relationships among the different variables. After that we pro-ceeded to our machine learning models divided into supervised and unsupervised learning algorithms.

The unsupervised learning algorithms utilised in our analysis are the PCA and the K-means clustering for dimensionality reduction and clustering purposes respectively. The optimal number of the PCA was 3 principal components which explain over 70% of the variance of our data and the optimal number of clusters was 4 clusters. 

As supervised algorithms we utilised the Linear Regression, Ridge, Decision Tree for Regression and Random Forest for Regression with rating as the re-sponse variable. The results of each model are evaluated from the evaluation metrics for regression models, the R-squared, MAE, MSE and RMSE. The per-formance of each model was displayed in figure 4.3.1 in which we can see that the Linear Regression has an R-squared of 5%, MAE equal to 0,39, MSE equal to 0,17 and RMSE equal to 0,41. The Ridge model has the same performance with the Linear Regression. The Decision Tree for Regression has an R-squared of 91%, MAE equal to 0,07, MSE equal to 0,02 and RMSE equal to 0,13. The final model provided the highest performance with an R-squared of 95%, MAE equal to 0,05, MSE equal to 0,01 and RMSE equal to 0,09. Finally, we kept the most important features using the Random Forest algorithm. In this phase we also ap-plied the XGboost for regression algorithm to keep only the features most strong-ly related to the variable of installs. 

However, the time needed for the Random Forest to be executed was 394,82 seconds and that is the reason why the next section of our project was about some optimization techniques. Hence, we applied the profiling technique in Py-thon and the NumPy library to optimize our analysis in terms of computational time without decreasing the accuracy of the models. The results revealed it is a good choice to use a more time efficient model, so we perform XGboost for Re-gression like previously. Indeed, the run time of the optimised XGboost model was shortened by 328,83 seconds compared to the Random Forest model without decreasing the accuracy of predicting ratings.

The main.py file encapsulates all the functions utilised in this project along with a parser that selects the model of the models selction module!

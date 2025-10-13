# GCP Serverless Cloud Function
## Lab Rules
I used the partial pressure of oxygen in the arterila blood(PaO2) as my lab value. The link below is my source and the chart that defines it. Anything that isn't normal(80 <= PaO2 <= 100) is labelled as abnormal.

Source: [PaO2 information](https://ecampusontario.pressbooks.pub/mechanicalventilators/chapter/oxygenation-status-the-final-piece/)

![PaO2 chart](/image/PaO2_chart.png)

Below are my publicly accessible endpoint URLs for each deployed function.

## Clouds, Regions, Auth
Google Cloud Run: 

Region: Europe-west1

Auth:Unauthenticated(public)

[https://po2-lab-results-226431719640.europe-west1.run.app](https://po2-lab-results-226431719640.europe-west1.run.app)


Azure Function:

Region: Canada Central
Auth: Key Based 

URL:
[https://pao2-lab-values-drd6gcgeapbufxeb.canadacentral-01.azurewebsites.net/api/http_trigger1?code=YS2RIO2lVYt0bdf61fYAH2QlfbccAYxEmj2T7ZqF6U0cAzFuSqM20g==](https://pao2-lab-values-drd6gcgeapbufxeb.canadacentral-01.azurewebsites.net/api/http_trigger1?code=YS2RIO2lVYt0bdf61fYAH2QlfbccAYxEmj2T7ZqF6U0cAzFuSqM20g==)


## GET/POST EXAMPLE REQUEST
#### GCP
![gcp_testing](../image/GCP_testing.png)
![gcp-url](../image/gcp_url.png)

#### Azure
![azure_testing](../image/azure_testing.png)
![azure-url](../image/azure_url.png)


## Loom URL Recording:



## Personal Comparison
Google Cloud Console was more intuitive and user-friendly compared to Microsoft Azure. Azure required more manual coding and configuration to achieve the same results as Google’s platform, and its generated URLs were notably longer and less streamlined. However, Google Cloud required deploying the source code before testing, which made the process more time-consuming. In contrast, Azure allowed for code testing prior to deployment, offering greater flexibility during development.
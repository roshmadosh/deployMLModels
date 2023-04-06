## Deploying your REST API through Microsoft Azure App Services
1. Fork the repo to your own github account.
2. From the Azure portal, look up `App Services` on the search bar and navigate to the service.
3. Click "create"
4. Fill out the first page.  
    - `Runtime stack` should be `Python 3.10`
    - `Pricing plan` must be `Basic` or better for Github deployment (this is not a free pricing plan. if you don't want to incur charges, remember to delete resources).
5. On the `Deployment` page, connect to the forked repository on your Github account.
6. Create the app service.
7. Once created, go to the resource and navigate to the `Configuration` setting.
8. Under the `General Settings` tab, copy and paste into the startup command:  
`gunicorn LVL4.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000`
9. Go back to the `Overview` section and restart the App Service.
10. Go to the `Overview` tab and click on the link under Default domain.


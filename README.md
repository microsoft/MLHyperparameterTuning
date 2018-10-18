# Requirements

This project is meant to run on Linux. 

# Setup

To set up your environment to run these notebooks, please follow these
steps.  They setup the notebooks to use Docker and Azure seamlessly.

1. Create a _Linux_ DSVM.
2. In a bash shell on the DSVM, add your login to the `docker` group:
   ```
   sudo usermod -a -G docker <login>
   ```
3. Login to your DockerHub account:
   ```
   docker login
   ```
4. Clone, fork, or download the zip file for this repository:
   ```
   git clone https://github.com/Azure/MLAKSDeployment.git
   ```
5. Create the Python MLAKSDeployment virtual environment using the environment.yml:
   ```
   conda env create -f environment.yml
   ```
6. Activate the virtual environment:
   ```
   source activate MLAKSDeployment
   ```
7. Login to Azure:
   ```
   az login
   ```
8. If you have more than one Azure subscription, select it:
   ```
   az account set --subscription <Your Azure Subscription>
   ```
9. Start the Jupyter notebook server in the virtual environment:
   ```
   jupyter notebook
   ```

# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

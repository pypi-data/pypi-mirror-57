from azure.mgmt.containerservice  import ContainerServiceClient
from azure.common.credentials import ServicePrincipalCredentials

def upgradeToLatestVersion(azure_credential,subscription,resource_group_name,resource_name):
    """ Upgrade AKS to the latest version (no preview)  
       Needs to be contributor on K8S cluster and on log analytics workspace linked to k8s """
    print("===Start : upgradeToLatestVersion===")
    print(subscription+'/'+resource_group_name+'/'+resource_name)
    K8sClient = ContainerServiceClient(azure_credential,subscription)
    upgradeProfile = K8sClient.managed_clusters.get_upgrade_profile(resource_group_name,resource_name)
    currentManagedCluster = K8sClient.managed_clusters.get(resource_group_name, resource_name)
    currentVersion=currentManagedCluster.kubernetes_version
    version=currentManagedCluster.kubernetes_version
    if upgradeProfile.control_plane_profile.upgrades :
     for upversion in upgradeProfile.control_plane_profile.upgrades:
      if not upversion.is_preview:
       if upversion.kubernetes_version > version:
        version = upversion.kubernetes_version
        currentManagedCluster.kubernetes_version = upversion.kubernetes_version
     if currentManagedCluster.provisioning_state == 'Succeeded' and version > currentVersion :
      print(subscription+'/'+resource_group_name+'/'+resource_name+'Upgrade from '+str(currentVersion)+' to '+str(version))  
      try:
          upgradedManagedCluster = K8sClient.managed_clusters.create_or_update(resource_group_name, resource_name,currentManagedCluster )
          print("done")
      except  Exception as e: 
          print("WARNING: - " +subscription+'/'+resource_group_name+'/'+resource_name+'Upgrade from '+str(currentVersion)+' to '+str(version)+': '+str(e))
     else:
        print('NO UPGRADE POSSIBLE '+currentVersion+' = '+version)
    else:
     print('NO UPGRADE POSSIBLE for '+subscription+'/'+resource_group_name+'/'+resource_name)
     print(upgradeProfile.control_plane_profile.kubernetes_version)
    print("===End : upgradeToLatestVersion===")


#updateServiceEndPointAzureRmCredential(credentials,organization_url, project, spnId,spnKey):
def updateSpnCluster(azure_credentials, subscription_id,resource_group_name, resource_name, graph_credentials, devops_credentials, organization_url, project):
 """ update Spn Cluster  """
 K8sClient = ContainerServiceClient(azure_credentials,subscription_id)
 cluster = K8sClient.managed_clusters.get(resource_group_name, resource_name)
 graph_credentials = ServicePrincipalCredentials(client_id = CLIENT,secret = KEY,tenant = TENANT_ID,resource = 'https://graph.windows.net')
 graphrbac_client = GraphRbacManagementClient(graph_credentials, TENANT_ID)
 listKeys = graphrbac_client.applications.list_password_credentials(getObjectIdFromAppId(TENANT_ID,graph_credentials,cluster.service_principal_profile.client_id ))


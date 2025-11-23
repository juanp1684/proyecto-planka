
import pytest
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from src.resources.payloads.project_payloads import PAYLOAD_PROJECT_CREATE 
from utils.logger_helper import log_request_response
from src.routes.request import PlankaRequests




@pytest.mark.project_management
@pytest.mark.e2e
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.headers_validation
def test_e2e_projects(setup_add_project,create_test_project):
   # =================================================
   #  Precondiciones: 
   # -  Usuario autenticado con credenciales validas
   # -  Token generado correctamente
   #=================================================
    

    # Creación de un nuevo proyecto con los datos establecidos para el trabajo del equipo

    url = EndpointPlanka.BASE_PROJECTS.value
    get_token , created_projects = setup_add_project
    headers = {'Authorization': f'Bearer {get_token}'}

    response = PlankaRequests.post(url,headers,PAYLOAD_PROJECT_CREATE)
    log_request_response(url, response, headers, PAYLOAD_PROJECT_CREATE)
    AssertionStatusCode.assert_status_code_200(response)
    created_projects.append(response.json())


     # Obtener proyecto creado recientemente

    response = PlankaRequests.get(url,headers)
    log_request_response(url, response, headers)
    AssertionStatusCode.assert_status_code_200(response)


     # Eliminar proyecto utilizado durante el flujo de trabajo
     
    project_id = create_test_project
    ID_PROJECT = project_id
    url = f"{EndpointPlanka.BASE_PROJECTS.value}/{ID_PROJECT}"
    response = PlankaRequests.delete(url,headers)
    log_request_response(url, response, headers)
    AssertionStatusCode.assert_status_code_200(response)
     


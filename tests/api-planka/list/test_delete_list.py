
import pytest
from utils.constans import TOKEN_INVALID ,ID_LIST_NOT_EXISTS,ID_LIST_EMPTY,ID_LIST_INVALID_STRING
from src.routes.endpoint import EndpointPlanka
from src.assertions.status_code_assertion import AssertionStatusCode
from utils.logger_helper import log_request_response
from src.routes.request import PlankaRequests


@pytest.mark.list
@pytest.mark.smoke
@pytest.mark.functional_positive
@pytest.mark.functional_negative
@pytest.mark.headers_validation
@pytest.mark.parametrize(
     "use_fixture,token_value,expected_status",
     [(True,None,200),
      (False,TOKEN_INVALID,401)
     ],
     ids=[
          "TC025: delete_list_with_valid_token",
          "TC026: delete_list_with_invalid_token"
     ])

def test_delete_list_with_token(get_token,create_test_list,use_fixture,token_value,expected_status):
   TOKEN_PLANKA =get_token if use_fixture else token_value
   ID_LIST = create_test_list
   url = f"{EndpointPlanka.BASE_LIST_MAJOR.value}/{ID_LIST}"
   headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
   response = PlankaRequests.delete(url,headers)
   log_request_response(url, response, headers)

   if expected_status == 200:
      AssertionStatusCode.assert_status_code_200(response)
   else:
      AssertionStatusCode.assert_status_code_401(response)




@pytest.mark.list
@pytest.mark.functional_negative
@pytest.mark.regression
@pytest.mark.equivalence_partition
@pytest.mark.parametrize(
   "id_list,expected_status",[
      pytest.param(ID_LIST_NOT_EXISTS,404,
                   id="TC027: delete_list_with_id_not_exists"),

      pytest.param(ID_LIST_EMPTY,400,
                   marks=pytest.mark.xfail(reason="BUG019 : Código HTTP incorrecto se retorna 404 en lugar de 400 al consultar un recurso vacio"),
                   id="TC028: delete_list_with_id_empty"),
      
      pytest.param(ID_LIST_INVALID_STRING,400,
                   id="TC029: delete_list_with_id_invalid_string")

   ])

def test_delete_list_with_id_parametrizer(get_token,id_list,expected_status):
   TOKEN_PLANKA = get_token
   url = f"{EndpointPlanka.BASE_LIST_MAJOR.value}/{id_list}"
   headers = {'Authorization': f'Bearer {TOKEN_PLANKA}'}
   response = PlankaRequests.delete(url,headers)
   log_request_response(url, response, headers)
   if expected_status == 404:
      AssertionStatusCode.assert_status_code_404(response)
   else:
      AssertionStatusCode.assert_status_code_400(response)





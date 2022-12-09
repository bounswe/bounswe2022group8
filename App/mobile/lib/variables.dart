import 'profile.dart';

const String HOST = "34.125.134.88:8000";
const String REGISTER_ENDPOINT = "http://$HOST/api/v1/auth/register/";
const String LOGIN_ENDPOINT = "http://$HOST/api/v1/auth/login/";
const String LOGOUT_ENDPOINT = "http://$HOST/api/v1/auth/logout/";
const String GET_ALL_ART_ITEM_ENDPOINT = "http://$HOST/api/v1/artitems/";
const String GET_PROFILE_ENDPOINT = "http://$HOST/api/v1/users/profile/me/" ;
const String UPLOAD_ART_ITEM_ENDPOINT = "http://$HOST/api/v1/artitems/me/upload/";
const String UPDATE_PROFILE_ENDPOINT = "http://$HOST/api/v1/users/profile/me/" ;
String GET_USER_ART_ITEM_ENDPOINT =  "http://$HOST/api/v1/artitems/users/username/$registered_username";
String GET_OTHER_PROFILE_ENDPOINT = "http://$HOST/api/v1/users/profile/" ;
const String OTP_ENDPOINT ="http://$HOST/api/v1/auth/request-reset/";
const String PASSWORD_RESET_ENDPOINT ="http://$HOST/api/v1/auth/password-reset/";

String token = "";
String registered_username = "";
String registered_password = "" ;
String registered_email = "";
String change_email = "";
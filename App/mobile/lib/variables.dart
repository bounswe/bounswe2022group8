import 'package:artopia/profile.dart';

const String HOST = "34.125.134.88:8000";
const String REGISTER_ENDPOINT = "http://$HOST/api/v1/auth/register/";
const String LOGIN_ENDPOINT = "http://$HOST/api/v1/auth/login/";
const String LOGOUT_ENDPOINT = "http://$HOST/api/v1/auth/logout/";
const String GET_ALL_ART_ITEM_ENDPOINT = "http://$HOST/api/v1/artitems/";
const String GET_PROFILE_ENDPOINT = "http://$HOST/api/v1/users/profile/me/" ;
String GET_USER_ART_ITEM_ENDPOINT =  "http://$HOST/api/v1/artitems/users/username/$registered_username";
String token = "";
String registered_username = "";
String registered_password = "" ;

String change_email = "";











const String OTP_ENDPOINT ="http://$HOST/api/v1/auth/request-reset/";
const String PASSWORD_RESET_ENDPOINT ="http://$HOST/api/v1/auth/password-reset/";

String registered_email = "";


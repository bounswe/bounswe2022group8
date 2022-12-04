import 'package:artopia/profile.dart';

const String HOST = "34.125.134.88:8000";
const String REGISTER_ENDPOINT = "http://$HOST/api/v1/auth/register/";
const String LOGIN_ENDPOINT = "http://$HOST/api/v1/auth/login/";
const String LOGOUT_ENDPOINT = "http://$HOST/api/v1/auth/logout/";
const String GET_PROFILE_ENDPOINT = "http://$HOST/api/v1/users/profile/me/" ;
String token = "";
String registered_username = "";
String registered_password = "" ;

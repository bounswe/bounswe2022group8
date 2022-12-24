import 'package:flutter/material.dart';
import 'home_page.dart';
import 'landing_page.dart';
import 'login_page.dart';
import 'package:image_downloader/image_downloader.dart';
import 'package:flutter/services.dart';
import 'dart:convert';

import 'package:aws_common/aws_common.dart';
import 'package:aws_signature_v4/aws_signature_v4.dart';

const AWSSigV4Signer signer = AWSSigV4Signer(
  credentialsProvider: AWSCredentialsProvider.environment(),
);

// Create the signing scope and HTTP request
const region = 'us-east-1';
Future<String> getImage(String path) async {

  final serviceConfiguration = S3ServiceConfiguration();

  final scope = AWSCredentialScope(
    region: region,
    service: AWSService.s3,
  );
  String host = 'cmpe451-production.s3.amazonaws.com';

final request = AWSHttpRequest.get(
    Uri.https(host, path),
    headers: {
      AWSHeaders.host: host,
    },
  );
  // Sign and send the HTTP request
  final signedUrl = await signer.presign(
    request,
    credentialScope: scope,
    serviceConfiguration: serviceConfiguration,
    expiresIn: const Duration(minutes: 10),
  );
  //safePrint('Download URL:' + signedUrl.toString());
  return(signedUrl.toString()) ;
}

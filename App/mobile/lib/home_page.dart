import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_app_mustafa/routes.dart';
import 'templates.dart';

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      child: Text('Ben bir homepage olacagim', style: TextStyle(color: Colors.white),),
    );
  }
}


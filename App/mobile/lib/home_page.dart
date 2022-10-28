import 'package:flutter/material.dart';
import 'package:flutter_app_mustafa/routes.dart';
import 'templates.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        leading: const Icon(Icons.account_circle_rounded),
        title: const Text(
          "MyApp",
          style:  TextStyle(
            color: Colors.black45,
            fontFamily: "OpenSans",
            fontSize: 30.0,
            fontWeight: FontWeight.bold,
            ),
          ),
        actions: const [
          Icon(Icons.more_vert),
          ],
        ),
      bottomNavigationBar: BottomNavigationBar(
        items: const [
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: 'Home',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.open_in_new_rounded),
            label: 'Logout',
          ),
        ],
        ),
      );
  }
}



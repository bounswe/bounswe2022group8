import 'package:flutter/material.dart';
import 'package:artopia/landing_page.dart';
import 'package:artopia/profile_page.dart';
import 'package:artopia/routes.dart';
import 'widgets/posts.dart';
import 'templates.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final EmailInputObject = EmailInput();
  final PasswordInputObject = PasswordInput(name: "Password");
  void goToProfile(BuildContext context) {
    Route route = MaterialPageRoute(builder: (context) => ProfilePage());
    Navigator.pushReplacement(context, route);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        leading: IconButton(
          icon: Icon(Icons.account_circle_rounded),
          tooltip: 'Go to your profile',
          onPressed: () => {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => ProfilePage()),
            )
          },
        ),
        title: const Text(
          "Artopia",
          style: TextStyle(
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
      body: SingleChildScrollView(
        scrollDirection: Axis.vertical,
        child: Column(
          children: [
            Container(
              margin: const EdgeInsets.only(right: 10),
              child: Column(
                children: [
                  PostsList(),
                ],
              ),
            ),
            Container(
              margin: const EdgeInsets.only(right: 10),
              child: Column(
                children: [
                  PostsList(),
                ],
              ),
            ),
            Container(
              margin: const EdgeInsets.only(right: 10),
              child: Column(
                children: [
                  PostsList(),
                ],
              ),
            ),
            Container(
              margin: const EdgeInsets.only(right: 10),
              child: Column(
                children: [
                  PostsList(),
                ],
              ),
            ),
          ],
        ),
      ),
      bottomNavigationBar: BottomNavigationBar(
        onTap: (value) {
          if (value == 1) {
            Route route =
                MaterialPageRoute(builder: (context) => LandingPage());
            Navigator.pushReplacement(context, route);
          }
        },
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

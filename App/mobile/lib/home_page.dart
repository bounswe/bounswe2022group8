import 'package:artopia/artitem.dart';
import 'package:artopia/utils/colorPalette.dart';
import 'package:flutter/material.dart';
import 'package:artopia/landing_page.dart';
import 'package:artopia/profile_page.dart';
import 'package:artopia/routes.dart';
import 'widgets/post.dart';
import 'templates.dart';
import 'package:artopia/utils/textUtils.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final textUtils = TextUtils();
  final ColorPalette colorPalette = ColorPalette();
  // Future<ArtItem> artitemfuture = getAllArtItems();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      // backgroundColor: colorPalette.darkPurple,
      appBar: PreferredSize(
        preferredSize: const Size.fromHeight(40.0),
        child: AppBar(
          centerTitle: true,
          automaticallyImplyLeading: false,
          backgroundColor: colorPalette.darkPurple,
          title: textUtils.buildText(
              "artopia", 25, Colors.white70, FontWeight.w500),
        ),
      ),
      body: FutureBuilder<List<ArtItem>>(
          future: getAllArtItems(),
          builder: (BuildContext context,
              AsyncSnapshot<List<ArtItem>> snapshot) {
            if (snapshot.hasData == false)
              return SizedBox.shrink();
            List<ArtItem> artItems = snapshot.requireData;

            return  SingleChildScrollView(
          scrollDirection: Axis.vertical,
          child: Column(
            children: [
              for (ArtItem item in artItems ) (Post(artitem: item))
            ],
          ),
    ) ;},),
      bottomNavigationBar: BottomNavigationBar(
        selectedItemColor: colorPalette.darkPurple,
        unselectedItemColor: colorPalette.darkPurple,
        onTap: (value) {
          setState(() {
          });
          if (value == 1) {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => ProfilePage()),
            );
          }
          if (value == 2) {
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
            icon: Icon(Icons.account_circle_rounded),
            label: 'Profile',
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

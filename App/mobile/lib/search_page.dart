import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:artopia/search.dart';
import 'package:artopia/utils/colorPalette.dart';
import 'package:artopia/utils/textUtils.dart';
import 'package:artopia/settings_page.dart';
import 'package:flutter/services.dart';
import 'package:artopia/home_page.dart';
import 'package:artopia/landing_page.dart';
import 'package:artopia/profile_page.dart';
import 'package:artopia/profile.dart';
import 'package:artopia/widgets/self_profile.dart';
import 'dart:core';

class SearchPage extends StatefulWidget {
  @override
  _SearchPageState createState() => _SearchPageState();
}

class _SearchPageState extends State<SearchPage> {
  Future<Profile> me = getMyProfile();
  final ColorPalette colorPalette = ColorPalette();
  final textUtils = TextUtils();
  String selectedUser = "";
  String selectedArtItem = "";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: PreferredSize(
        preferredSize: Size.fromHeight(40),
        child: Container(
          decoration: BoxDecoration(
            border: Border(
              bottom: BorderSide(
                width: 1,
                color: colorPalette.darkPurple,
              ),
            ),
          ),
          child: AppBar(
            centerTitle: true,
            automaticallyImplyLeading: false,
            backgroundColor: colorPalette.darkPurple,
            title: textUtils.buildText(
                "artopia", 25, Colors.white70, FontWeight.w500),
            actions: [
              IconButton(
                icon: Icon(Icons.settings),
                color: colorPalette.russianGreen,
                tooltip: 'Settings',
                onPressed: () => {
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => SettingsPage()),
                  ),
                },
              ),
            ],
          ),
        ),
      ),
      body: Column(
        children: <Widget>[
          Row(mainAxisAlignment: MainAxisAlignment.center, children: <Widget>[
            SizedBox(
              //User Search
              width: MediaQuery.of(context).size.width / 2.1,
              child: OutlinedButton.icon(
                label: textUtils.buildText(
                    "User Search", 17, Colors.white70, FontWeight.w500),
                icon: Icon(Icons.search, size: 17),
                style: OutlinedButton.styleFrom(
                  foregroundColor: Colors.white,
                  backgroundColor: colorPalette.darkPurple,
                  side: BorderSide(
                    color: colorPalette.darkPurple,
                  ),
                ),
                onPressed: () async {
                  final finalResult = await showSearch(
                    context: context,
                    delegate: Search(
                      allCaliforniaPlaces: allCaliforniaLocations,
                      californiaPlaceSuggestion: popularCaliforniaLocations,
                    ),
                  );
                  setState(
                    () {
                      selectedUser = finalResult!;
                      Route route =
                      MaterialPageRoute(builder: (context) => ProfilePage());
                      Navigator.pushReplacement(context, route);
                    },
                  );
                },
              ),
            ),
            SizedBox(width: 10),
            SizedBox(
              //Art Item Search
              width: MediaQuery.of(context).size.width / 2.1,
              child: OutlinedButton.icon(
                label: textUtils.buildText(
                    "Art Item Search", 17, Colors.white70, FontWeight.w500),
                icon: Icon(Icons.search, size: 17),
                style: OutlinedButton.styleFrom(
                  foregroundColor: Colors.white,
                  backgroundColor: colorPalette.darkPurple,
                  side: BorderSide(
                    color: colorPalette.darkPurple,
                  ),
                ),
                onPressed: () async {
                  final finalResult = await showSearch(
                    context: context,
                    delegate: Search(
                      allCaliforniaPlaces: allCaliforniaLocations,
                      californiaPlaceSuggestion: popularCaliforniaLocations,
                    ),
                  );
                  setState(
                    () {
                      selectedArtItem = finalResult!;
                    },
                  );
                },
              ),
            ),
          ]),
          /*
          selectedUser == ""
              ? SizedBox.shrink()
              :
              //SizedBox.shrink(),
          Container(),
          */


          /*
          Container(
                  padding: EdgeInsets.symmetric(horizontal: 35, vertical: 15),
                  color: colorPalette.darkPurple,
                  child: textUtils.buildText(
                      selectedUser, 18, Colors.white70, FontWeight.w500),
          ),
          */
          /*
          Expanded(
            child: ListView.builder(
              itemCount: allCaliforniaLocations.length,
              itemBuilder: (context, index) {
                return ListTile(
                  title: Text(allCaliforniaLocations[index]),
                );
              },
            ),
          ),
          */
        ],
      ),
      bottomNavigationBar: BottomNavigationBar(
        type: BottomNavigationBarType.fixed,
        iconSize: 24,
        selectedItemColor: colorPalette.darkPurple,
        unselectedItemColor: colorPalette.darkPurple,
        onTap: (value) {
          if (value == 0) {
            Route route = MaterialPageRoute(builder: (context) => HomePage());
            Navigator.pushReplacement(context, route);
          } else if (value == 1) {
            Route route =
                MaterialPageRoute(builder: (context) => ProfilePage());
            Navigator.pushReplacement(context, route);
          } else if (value == 3) {
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
            icon: Icon(Icons.search),
            label: 'Search',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.open_in_new_rounded),
            label: 'Logout',
          ),
        ],
      ),
    );
  }

  otherProfile(BuildContext context, me) {}
}

final List<String> allCaliforniaLocations = [
  "Alameda",
  "Albany",
  "Alhambra",
  "Aliso Viejo",
  "Alturas",
  "Amador City",
  "American Canyon",
  "Anaheim",
  "Anderson",
  "Angels Camp",
  "Antioch",
  "Apple Valley",
  "Arcadia",
  "Arcata",
  "Arroyo Grande",
  "Artesia",
  "Arvin",
  "Atascadero",
  "Atwater",
  "Auburn",
  "Avalon",
  "Avenal",
  "Azusa",
  "Bakersfield",
  "Baldwin Park",
  "Banning",
  "Barstow",
  "Beaumont",
  "Bell",
  "Bell Gardens",
  "Bellflower",
  "Belmont",
  "Belvedere",
  "Benicia",
  "Berkeley",
  "Beverly Hills",
  "Big Bear Lake",
  "Biggs",
  "Bishop",
  "Bloomington",
  "Blythe",
  "Bodega Bay",
  "Brawley",
  "Brea",
  "Brentwood",
  "Brisbane",
  "Buellton",
  "Buena Park",
  "Burbank",
  "Burlingame",
  "Buttonwillow",
  "Byron",
  "Calexico",
  "Calimesa",
  "Calipatria",
];
final List<String> popularCaliforniaLocations = [
  "Alameda",
  "Albany",
  "Antioch",
  "Apple Valley",
  "Arcadia",
  "Bakersfield",
  "Baldwin Park",
  "Beaumont",
  "Bell",
  "Bell Gardens",
  "Bellflower",
  "Belmont",
  "Belvedere",
  "Benicia",
  "Berkeley",
  "Beverly Hills",
  "Brentwood",
  "Brisbane",
  "Buellton",
  "Buena Park",
  "Burbank",
  "Calimesa",
  "Calipatria",
];

import 'package:artopia/art_items_tab.dart';
import 'package:artopia/routes.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:artopia/home_page.dart';
import 'package:artopia/landing_page.dart';
import 'profile.dart';
import 'package:artopia/widgets/profile_header_widgets.dart';
import 'package:artopia/utils/colorPalette.dart';
import 'package:artopia/utils/textUtils.dart';
import 'package:artopia/settings_page.dart';

class ProfilePage extends StatefulWidget {
  const ProfilePage({Key? key}) : super(key: key);

  @override
  State<ProfilePage> createState() => _ProfilePageState();
}

class _ProfilePageState extends State<ProfilePage> {
  final ColorPalette colorPalette = ColorPalette();
  final textUtils = TextUtils();
  Future<Profile> myProfile = getMyProfile() ;  
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
                color: Colors.black,
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
      body: DefaultTabController(
        length: 2,
        child:FutureBuilder<Profile>(
          future: myProfile, // a previously-obtained Future<String> or null
          builder: (BuildContext context, AsyncSnapshot<Profile> snapshot) {
            if(snapshot.hasData == false)   return SizedBox.shrink();
            final Profile me = snapshot.requireData ;
          return NestedScrollView(
          headerSliverBuilder: (context, _) {
            return [
              SliverList(
                delegate: SliverChildListDelegate(
                  [
                   profileHeaderWidget(context,me),
                  ],
                ),
              ),
            ];
          },
          body: Column(
            children: <Widget>[
              Material(
                color: colorPalette.blackShadows,
                child: TabBar(
                  padding: const EdgeInsets.only(left: 0),
                  labelColor: Colors.black,
                  //unselectedLabelColor: Colors.grey[400],
                  indicatorWeight: 3,
                  indicatorColor: colorPalette.darkPurple,
                  tabs: [
                    Container(
                      alignment: Alignment.center,
                      height: 40,
                      child: textUtils.buildText(
                          "Art Items", 15, colorPalette.darkPurple, FontWeight.w500
                      ),
                    ),
                    Container(
                      alignment: Alignment.center,
                      height: 40,
                      child: textUtils.buildText(
                          "Exibitions", 15, colorPalette.darkPurple, FontWeight.w500
                      ),
                    ),
                  ],
                ),
              ),
              Expanded(
                child: TabBarView(
                  children: [
                    ArtItems(),
                    ArtItems(),
                    //Exibitions(),
                  ],
                ),
              ),
            ],
          ),
        );


  }, 
  ),
      ),
      bottomNavigationBar: BottomNavigationBar(
        selectedItemColor: colorPalette.darkPurple,
        unselectedItemColor: colorPalette.darkPurple,
        onTap: (value) {
          print(value);
          if (value == 0) {
            Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => HomePage()),
            );
          }
          else if (value == 2) {
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

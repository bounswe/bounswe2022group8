//import 'package:profile/profile.dart';
import 'package:artopia/art_items_tab.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:artopia/home_page.dart';
import 'package:artopia/routes.dart';
import 'package:artopia/profile.dart';
import 'package:artopia/widgets/profile_header_widgets.dart';
import 'package:artopia/utils/colorPalette.dart';
import 'templates.dart';
import 'register.dart';

class ProfilePage extends StatefulWidget {
  const ProfilePage({Key? key}) : super(key: key);

  @override
  State<ProfilePage> createState() => _ProfilePageState();
}

class _ProfilePageState extends State<ProfilePage> {
  final ColorPalette colorPalette = ColorPalette();
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
            leading: IconButton(
              icon: Icon(Icons.arrow_back),
              color: Colors.black,
              tooltip: 'Back to home page',
              onPressed: () => {
                Navigator.pop(
                  context,
                  MaterialPageRoute(builder: (context) => HomePage()),
                )
              },
            ),
            backgroundColor: colorPalette.graniteGray,
            actions: [
              IconButton(
                icon: Icon(Icons.settings),
                color: Colors.black,
                tooltip: 'Settings',
                onPressed: () => {
                  Navigator.pop(
                    context,
                    //MaterialPageRoute(builder: (context) => //SettingsPage()),
                  )
                },
              ),
            ],
          ),
        ),
      ),
      body: DefaultTabController(
        length: 2,
        child: NestedScrollView(
          headerSliverBuilder: (context, _) {
            return [
              SliverList(
                delegate: SliverChildListDelegate(
                  [
                    profileHeaderWidget(context),
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
                      child: Text(
                        "Art Items",
                        textAlign: TextAlign.center,
                        style: const TextStyle(
                          color: Colors.black87,
                          fontFamily: "OpenSans",
                          fontSize: 15.0,
                          //fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                    Container(
                      alignment: Alignment.center,
                      height: 40,
                      child: Text(
                        "Exibitions",
                        textAlign: TextAlign.center,
                        style: const TextStyle(
                          color: Colors.black87,
                          fontFamily: "OpenSans",
                          fontSize: 15.0,
                          //fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                  ],
                ),
              ),
              Expanded(
                child: TabBarView(
                  children: [
                    Gallery(),
                    Gallery(),
                    //ArtItems(),
                    //Exibitions(),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

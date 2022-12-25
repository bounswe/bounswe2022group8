import 'package:artopia/variables.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:artopia/home_page.dart';
import 'package:artopia/landing_page.dart';
import 'profile.dart';
import 'package:artopia/widgets/self_profile.dart';
import 'package:artopia/utils/colorPalette.dart';
import 'package:artopia/utils/textUtils.dart';
import 'package:artopia/settings_page.dart';
import 'package:artopia/art_items_tab.dart';
import 'package:artopia/exhibitions_tab.dart';
import 'package:flutter/cupertino.dart';
import 'dart:core';
import 'package:avatar_glow/avatar_glow.dart';
import 'package:dotted_border/dotted_border.dart';

class ProfilePage extends StatefulWidget {
  const ProfilePage({Key? key}) : super(key: key);

  @override
  State<ProfilePage> createState() => _ProfilePageState();
}

class _ProfilePageState extends State<ProfilePage> {
  final ColorPalette colorPalette = ColorPalette();
  final textUtils = TextUtils();
  Future<Profile> myProfile = getMyProfile() ;
  List<bool> isSelected = [true, false];
  bool isButtonPressed = false;
  int flag = 0;

  @override
  void initState() {
    isSelected = [true, false];
    super.initState();
  }

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
      body:
      DefaultTabController(
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
                    selfProfile(context,me),
                    //otherProfile(context,me),
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
                          "Exhibitions", 15, colorPalette.darkPurple, FontWeight.w500
                      ),
                    ),
                  ],
                ),
              ),
              Expanded(
                child: TabBarView(
                  children: [
                    ArtItems(),
                    Exhibitions()
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
              token = "" ;
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

  otherProfile(BuildContext context, Profile user) {

    return Container(

      width: double.infinity,
      decoration: BoxDecoration(
        color: colorPalette.graniteGray,
      ),
      child: Padding(
        padding: const EdgeInsets.only(left: 18.0, right: 18.0, bottom: 10),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.start,
              children: [
                Padding(padding: const EdgeInsets.only(left: 5)),
                Column(
                  children: [
                    SizedBox(
                      width: 120,
                      height: 120,
                      child: AvatarGlow(
                        glowColor: colorPalette.darkPurple,
                        endRadius: 90.0,
                        duration: Duration(milliseconds: 2000),
                        repeat: true,
                        showTwoGlows: true,
                        repeatPauseDuration: Duration(milliseconds: 100),
                        child: DottedBorder(
                          radius: Radius.circular(5),
                          color: colorPalette.darkPurple,
                          strokeWidth: 8,
                          borderType: BorderType.Circle,
                          dashPattern: [1, 12],
                          strokeCap: StrokeCap.butt,
                          child: Center(
                            child: SizedBox(
                              width: 130,
                              height: 130,
                              child: CircleAvatar(


                                foregroundImage: Image
                                    .network(
                                    user.imageUrl)

                                    .image,
                                radius: 10,

                              ),
                            ),
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
                Padding(padding: const EdgeInsets.only(left: 20)),
                Column(
                  mainAxisSize: MainAxisSize.min,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    SizedBox(height: 20),
                    Row(
                      children: [
                        textUtils.buildText(
                            user.username, 18, Colors.white70, FontWeight.w500
                        ),
                      ],
                    ),
                    SizedBox(height: 5),
                    Row(
                      children: [
                        textUtils.buildText(
                            user.name, 13, Colors.white70, FontWeight.w500
                        ),
                      ],
                    ),
                    SizedBox(height: 15),
                    Container(
                      //padding: const EdgeInsets.all(16.0),
                      width: 200,
                      //width: MediaQuery.of(context).size.width*0.8,
                      child: textUtils.buildText(
                          user.bio, 12, Colors.white70, FontWeight.w500
                      ),
                    ),


                    SizedBox(height: 15),
                    Row(
                      children: [
                        Wrap(
                          crossAxisAlignment: WrapCrossAlignment.center,
                          children: [
                            Icon(Icons.location_on),
                            textUtils.buildText(
                                user.location, 12, Colors.white70, FontWeight.w500
                            ),
                          ],
                        ),
                      ],
                    ),
                    SizedBox(height: 10),
                    Row(
                      crossAxisAlignment: CrossAxisAlignment.center,
                      children: [
                        GestureDetector(
                          child: textUtils.buildText(
                              "Followers ", 12, Colors.black87, FontWeight.w500
                          ),
                          onTap: () =>
                              Navigator.push(
                                context,
                                MaterialPageRoute(builder: (context) =>
                                    HomePage()),
                              ),
                        ),
                        textUtils.buildText(
                            user.followers.toString(), 13, Colors.black,
                            FontWeight.w500
                        ),
                        SizedBox(width: 20),
                        GestureDetector(

                          child:
                          textUtils.buildText(
                              " Following ", 12, Colors.black87, FontWeight.w500
                          ),
                          onTap: () =>
                              Navigator.push(
                                context,
                                MaterialPageRoute(builder: (context) =>
                                    HomePage()),
                              ),
                        ),
                        textUtils.buildText(
                            user.following.toString(), 13, Colors.black,
                            FontWeight.w500
                        ),
                      ],
                    ),
                  ],
                )
              ],
            ),
            const Padding(padding: const EdgeInsets.only(top: 10)),
            Row(
              mainAxisAlignment: MainAxisAlignment.start,
              children: [
                Padding(
                  padding: EdgeInsets.only(left: 10),
                  child:
                      Container(
                        width: 100,
                        height: 30,
                        child:
                        ElevatedButton(
                          onPressed: () async {
                            setState(() {
                              if(isButtonPressed == false){
                                if(flag == 0){
                                  user.followers = user.followers + 1;
                                  flag = flag + 1;
                                }
                              }
                              else{
                                if(flag > 0){
                                  user.followers = user.followers - 1;
                                  flag= 0;
                                }
                              }
                              isButtonPressed = !isButtonPressed;
                            });
                          },
                          style: isButtonPressed ? ElevatedButton.styleFrom(//pressed
                            backgroundColor: colorPalette.frenchLilac,
                            foregroundColor: Colors.black,
                            shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(10.0),
                            ),
                          ) :
                          ElevatedButton.styleFrom(//not_pressed
                            backgroundColor: colorPalette.blackShadows,
                            foregroundColor: Colors.black,
                            shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(10.0),
                            ),
                          ),
                          child:
                          Container(
                            height: 30,
                            width: 65,
                            child: Center(
                                child: isButtonPressed ? textUtils.buildText(
                                    "Following", 13, Colors.white, FontWeight.w500
                                ) :
                                textUtils.buildText(
                                    "Follow", 13, Colors.white, FontWeight.w500
                                )
                            ),
                          ),
                        ),
                      ),





                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

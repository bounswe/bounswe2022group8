import 'package:artopia/art_items_tab.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:artopia/home_page.dart';
import 'package:artopia/landing_page.dart';
import 'profile.dart';
import 'package:artopia/routes.dart';
import 'package:artopia/widgets/profile_header_widgets.dart';
import 'package:artopia/utils/colorPalette.dart';
import 'package:artopia/utils/textUtils.dart';
import 'package:artopia/profile_page.dart';
import 'package:artopia/profile.dart';

class SettingsPage extends StatefulWidget {
  const SettingsPage({Key? key}) : super(key: key);

  @override
  State<SettingsPage> createState() => _SettingsPageState();
}

class _SettingsPageState extends State<SettingsPage> {
  final ColorPalette colorPalette = ColorPalette();
  final textUtils = TextUtils();
  Future<Profile> myProfile = getMyProfile();
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
            leading: IconButton(
              icon: Icon(Icons.arrow_back),
              color: Colors.black,
              tooltip: 'Back to profile page',
              onPressed: () => {
                Navigator.pop(
                  context,
                  MaterialPageRoute(builder: (context) => ProfilePage()),
                )
              },
            ),
            title: textUtils.buildText(
                "artopia", 25, Colors.white70, FontWeight.w500),
          ),
        ),
      ),
      body:
        Container(),
    );
  }
}

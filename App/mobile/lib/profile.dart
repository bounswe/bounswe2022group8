import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:artopia/home_page.dart';
import 'package:artopia/routes.dart';
import 'package:artopia/profile.dart';
import 'package:artopia/profile_page.dart';
import 'package:artopia/templates.dart';
import 'package:artopia/register.dart';
import 'dart:core';
import 'package:avatar_glow/avatar_glow.dart';
import 'package:dotted_border/dotted_border.dart';
import 'package:url_launcher/url_launcher.dart';

class Profile extends StatefulWidget {
  Profile({
    required this.imageUrl,
    required this.username,
    required this.name,
    required this.bio,
    required this.location,
    required this.followers,
    required this.following,
  });
  final String imageUrl;
  final String username;
  final String name;
  final String bio;
  final String location;
  final String followers;
  final String following;

  @override
  State<Profile> createState() => _ProfileState();
}

class _ProfileState extends State<Profile> {
  @override
  Widget build(BuildContext context) {
    final Uri imagelUrl = Uri.parse(widget.imageUrl);
    final Uri usernameUrl = Uri.parse(widget.username);
    final Uri nameUrl = Uri.parse(widget.name);
    final Uri bioUrl = Uri.parse(widget.bio);
    final Uri locationUrl = Uri.parse(widget.location);
    final Uri followersUrl = Uri.parse(widget.followers);
    final Uri followingUrl = Uri.parse(widget.following);
    void getUrlLauncher(Uri url) async {
      if (await canLaunchUrl(url)) {
        await launchUrl(url);
      } else {
        throw 'Could not launch $url';
      }
    }

    return Container();
  }
}

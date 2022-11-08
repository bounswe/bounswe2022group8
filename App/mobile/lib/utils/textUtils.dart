import 'package:google_fonts/google_fonts.dart';
import 'package:flutter/material.dart';

class TextUtils{
  Text buildText(String text, double fontSize,Color color, FontWeight fontWeight) {
    return Text(
      text,
      style: GoogleFonts.inter(
        fontSize: fontSize,
        color: color,
        fontWeight: fontWeight,
      ),
    );
  }
}

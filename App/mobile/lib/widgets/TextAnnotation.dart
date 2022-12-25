import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:text_selection_controls/text_selection_controls.dart';
import '../utils/colorPalette.dart';

class Annotation {
  String annotationMessage;
  int annotationX;
  int annotationY;

  Annotation(this.annotationMessage, this.annotationX, this.annotationY);
}

class AnnotableTextField extends StatefulWidget {
  final String descriptionText;
  const AnnotableTextField({Key? key, required this.descriptionText})
      : super(key: key);

  @override
  State<AnnotableTextField> createState() => _AnnotableTextFieldState();
}

class _AnnotableTextFieldState extends State<AnnotableTextField> {
  final ColorPalette colorPalette = ColorPalette();

  @override
  Widget build(BuildContext context) {
    List<TextSpan> chars = [];

    for (int i = 0; i < widget.descriptionText.length; i++) {
      chars.add(TextSpan(
        text: widget.descriptionText[i],
      ));
    }
    return SelectableText.rich(
      TextSpan(
        children: chars,
        style: GoogleFonts.inter(
          fontSize: 20,
          color: colorPalette.blackShadows,
          fontWeight: FontWeight.w600,
          ),
        ),
      selectionControls: FlutterSelectionControls(toolBarItems: [
        ToolBarItem(
            item: Text(
              'Select All',
              style: GoogleFonts.inter(
                fontSize: 20,
                color: colorPalette.blackShadows,
                fontWeight: FontWeight.w600,
              ),
            ),
            itemControl: ToolBarItemControl.selectAll),
      ])
      );
  }
}
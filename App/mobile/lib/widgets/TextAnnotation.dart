import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:text_selection_controls/text_selection_controls.dart';
import '../utils/colorPalette.dart';

class Annotation {
  String userName;
  String annotationMessage;
  int annotationX;
  int annotationY;

  Annotation(this.userName, this.annotationMessage, this.annotationX,
      this.annotationY);
}

late String descriptionText;
bool annotationSelected = false;

class AnnotableTextField extends StatefulWidget {
  AnnotableTextField(
    String text,
    bool selection, {
    Key? key,
  }) : super(key: key) {
    descriptionText = text;
    annotationSelected = selection;
  }

  @override
  State<AnnotableTextField> createState() => _AnnotableTextFieldState();
}

class _AnnotableTextFieldState extends State<AnnotableTextField> {
  final ColorPalette colorPalette = ColorPalette();

  //holds annotations of every character
  final List<List<Annotation>> charAnnotations = List.generate(descriptionText.length, (index) => List.empty(growable: true));

  //selected texts. 0 means not selected, 1 means selected and 2 means there exists more than one annotation
  final List<bool> isAnnotatedChar = List.filled(descriptionText.length, false);


  @override
  Widget build(BuildContext context) {
    List<TextSpan> chars = [];


    /*
    THIS METHOD IS ONLY FOR TESTING PURPOSES
    ANNOTATIONS ARE NOT SAVED IN THE MOBILE SYSTEM
    THERE SHOULD BE API CALL TO GET ANNOTATIONS
    THERE SHOULD BE API CALL TO SAVE ANNOTATIONS
    AFTER GETTING ANNOTATIONS FROM API, THIS METHOD SHOULD BE CALLED TO FILL THE charAnnotations LIST AND isAnnotatedChar LIST
     */
    void addAnnotation(String annotationMessage,int start, int end) {
      String selectedText = descriptionText.substring(start, end);
      setState(() {
        for (int i = start; i < end; i++) {
          charAnnotations[i].add(Annotation("user", annotationMessage, i, i));
          isAnnotatedChar[i] = true;
        }
      });
      }

    GestureRecognizer? returnRecognizer(int i) {
      return TapGestureRecognizer()..onTap = () {
        showDialog(
          context: context,
          builder: (BuildContext context) {
            return AlertDialog(
              title: Text("Annotation"),
              content: Text(charAnnotations[i][0].annotationMessage),
              actions: [
                TextButton(
                  child: Text("Close"),
                  onPressed: () {
                    Navigator.of(context).pop();
                  },
                ),
              ],
            );
          },
        );
      };
    }

    for (int i = 0; i < descriptionText.length; i++) {
      chars.add(TextSpan(
        text: descriptionText[i],
        style: GoogleFonts.inter(
          textStyle: GoogleFonts.inter(
            fontSize: 20,
            color: colorPalette.blackShadows,
            fontWeight: FontWeight.w600,
            backgroundColor: (isAnnotatedChar[i] && annotationSelected)
                ? Colors.yellow
                : Colors.transparent,
          ),
        ),
        recognizer: (isAnnotatedChar[i] && annotationSelected) ? returnRecognizer(i) : null,
      ));
    }


    AlertDialog AnnotationDialog(String substring, int annotationX, int annotationY, BuildContext context) {
      final TextEditingController controller = TextEditingController();
      return AlertDialog(
        title: const Text("Annotation"),
        content: TextField(
          decoration: const InputDecoration(
            border: OutlineInputBorder(),
            labelText: 'Annotation',
          ),
          controller: controller,
        ),
        actions: <Widget>[
          TextButton(
            child: const Text("Cancel"),
            onPressed: () {
              Navigator.of(context).pop();
            },
          ),
          TextButton(
            child: const Text("Submit"),
            onPressed: () {
              addAnnotation(controller.text, annotationX, annotationY);
              Navigator.of(context).pop();
              //TODO: Add annotation to the database
            },
          ),
        ],
      );
    }

    setState(() {
      for(int i = 0; i < charAnnotations.length; i++){
        if(charAnnotations[i].isNotEmpty){
          isAnnotatedChar[i] = true;
        }
      }
    });



    return SelectableText.rich(
      TextSpan(
        children: chars,
        style: GoogleFonts.inter(
          fontSize: 20,
          color: colorPalette.blackShadows,
          fontWeight: FontWeight.w600,
        ),
      ),
      // selectionControls: MyMaterialTextSelectionControls(),
      selectionControls: FlutterSelectionControls(toolBarItems: [
        ToolBarItem(
            item: const Text(
              'Copy',
            ),
            itemControl: ToolBarItemControl.copy),
        annotationSelected ? ToolBarItem(
            item: const Text(
              'Select All',
            ),
            itemControl: ToolBarItemControl.selectAll) :
        ToolBarItem(
          item: const Text(
            'Annotate',
          ),
          onItemPressed: (String substring, int annotationX, int annotationY) {
            showDialog(
                context: context,
                builder: (BuildContext context) {
                  return AnnotationDialog(
                      substring, annotationX, annotationY, context);
                });
          },
        )
      ]),
    );
  }
}

/*

class MyMaterialTextSelectionControls extends MaterialTextSelectionControls {
  // Padding between the toolbar and the anchor.
  static const double _kToolbarContentDistanceBelow = 10.0;
  static const double _kToolbarContentDistance = 8.0;

  /// Builder for material-style copy/paste text selection toolbar.
  @override
  Widget buildToolbar(
      BuildContext context,
      Rect globalEditableRegion,
      double textLineHeight,
      Offset selectionMidpoint,
      List<TextSelectionPoint> endpoints,
      TextSelectionDelegate delegate,
      ClipboardStatusNotifier? clipboardStatus,
      Offset? lastSecondaryTapDownPosition,
      ) {
    final TextSelectionPoint startTextSelectionPoint = endpoints[0];
    final TextSelectionPoint endTextSelectionPoint =
    endpoints.length > 1 ? endpoints[1] : endpoints[0];
    final Offset anchorAbove = Offset(
      globalEditableRegion.left + selectionMidpoint.dx,
      globalEditableRegion.top +
          startTextSelectionPoint.point.dy -
          textLineHeight -
          _kToolbarContentDistance,
    );
    final Offset anchorBelow = Offset(
      globalEditableRegion.left + selectionMidpoint.dx,
      globalEditableRegion.top +
          endTextSelectionPoint.point.dy +
          _kToolbarContentDistanceBelow,
    );
    final value = delegate.textEditingValue;
    return MyTextSelectionToolbar(
      anchorAbove: anchorAbove,
      anchorBelow: anchorBelow,
      clipboardStatus: clipboardStatus,
      handleCustomButton: () {
        print(value.selection.textInside(value.text));
        delegate.hideToolbar();
      },
    );
  }
}

class MyTextSelectionToolbar extends StatelessWidget {
  const MyTextSelectionToolbar({
    Key? key,
    required this.anchorAbove,
    required this.anchorBelow,
    required this.clipboardStatus,
    required this.handleCustomButton,
  }) : super(key: key);

  final Offset anchorAbove;
  final Offset anchorBelow;
  final ClipboardStatusNotifier? clipboardStatus;
  final VoidCallback? handleCustomButton;

  @override
  Widget build(BuildContext context) {
    assert(debugCheckHasMaterialLocalizations(context));

    final List<_TextSelectionToolbarItemData> items =
    <_TextSelectionToolbarItemData>[
      _TextSelectionToolbarItemData(
        onPressed: handleCustomButton ?? () {},
        label: 'Custom button',
      ),
    ];

    int childIndex = 0;
    return TextSelectionToolbar(
      anchorAbove: anchorAbove,
      anchorBelow: anchorBelow,
      toolbarBuilder: (BuildContext context, Widget child) =>
          Container(color: Colors.pink, child: child),
      children: items
          .map((_TextSelectionToolbarItemData itemData) =>
          TextSelectionToolbarTextButton(
            padding: TextSelectionToolbarTextButton.getPadding(
                childIndex++, items.length),
            onPressed: itemData.onPressed,
            child: Text(itemData.label),
          ))
          .toList(),
    );
  }
}

class _TextSelectionToolbarItemData {
  const _TextSelectionToolbarItemData({
    required this.label,
    required this.onPressed,
  });

  final String label;
  final VoidCallback onPressed;
}

 */

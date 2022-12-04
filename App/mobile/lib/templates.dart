import 'package:flutter/material.dart';
import 'package:artopia/home_page.dart';
import 'package:artopia/login_page.dart';
import 'package:artopia/utils/textUtils.dart';
import 'package:artopia/utils/colorPalette.dart';
import 'package:google_fonts/google_fonts.dart';

class UsernameInput extends StatefulWidget {
  final usernameController = TextEditingController();
  UsernameInput({Key? key}) : super(key: key);

  @override
  State<UsernameInput> createState() => _UsernameInputState();
}

class _UsernameInputState extends State<UsernameInput> {
  final textUtils = TextUtils();
  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        textUtils.buildText(
            "Username",
            18,
            Colors.white,
            FontWeight.bold),
        const SizedBox(height: 10.0),
        Container(
          alignment: Alignment.centerLeft,
          decoration: BoxDecoration(
            color: const Color.fromARGB(120, 175, 180, 255),
            borderRadius: BorderRadius.circular(10),
          ),
          height: 60,
          child: TextField(
            controller: widget.usernameController,
            keyboardType: TextInputType.name,
            style: const TextStyle(color: Colors.white),
            decoration: InputDecoration(
                border: InputBorder.none,
                contentPadding: const EdgeInsets.only(top: 14),
                prefixIcon: const Icon(
                  Icons.email,
                  color: Colors.white,
                ),
                hintText: "Enter your username",
                hintStyle: GoogleFonts.inter(
                    fontSize: 14,
                    color: Colors.white54,
                ),
            ),
          ),
        ),
      ],
    );
  }
}

class EmailInput extends StatefulWidget {
  EmailInput({super.key});
  final emailController = TextEditingController();

  @override
  State<EmailInput> createState() => _EmailInputState();
}

class _EmailInputState extends State<EmailInput> {
  final TextUtils textUtils = TextUtils();
  final ColorPalette colorPalette = ColorPalette();
  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[

        textUtils.buildText("Email", 14,
            Colors.white, FontWeight.bold),
        const SizedBox(height: 10.0),
        Container(
          alignment: Alignment.centerLeft,
          decoration: BoxDecoration(
            color: const Color.fromARGB(120, 175, 180, 255),
            borderRadius: BorderRadius.circular(10),
          ),
          height: 60,
          child: TextField(
            controller: widget.emailController,
            keyboardType: TextInputType.emailAddress,
            style: const TextStyle(color: Colors.white),
            decoration:  InputDecoration(
                border: InputBorder.none,
                contentPadding: const EdgeInsets.only(top: 14),
                prefixIcon: const Icon(
                  Icons.email,
                  color: Colors.white,
                ),
                hintText: "Enter your email",
                hintStyle: GoogleFonts.inter(
                  fontSize: 14,
                  color: Colors.white54,
                )),
          ),
        ),
      ],
    );
  }
}

class PasswordInput extends StatefulWidget {
  final String name;
  PasswordInput({Key? key, required this.name}) : super(key: key);
  final passwordController = TextEditingController();
  @override
  State<PasswordInput> createState() => _PasswordInputState();
}

class _PasswordInputState extends State<PasswordInput> {
  final TextUtils textUtils = TextUtils();
  final ColorPalette colorPalette = ColorPalette();
  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        textUtils.buildText(widget.name, 14,
            Colors.white, FontWeight.bold),
        const SizedBox(height: 10.0),
        Container(
          alignment: Alignment.centerLeft,
          decoration: BoxDecoration(
            color: const Color.fromARGB(120, 175, 180, 255),
            borderRadius: BorderRadius.circular(10),
          ),
          height: 60,
          child: TextField(
            controller: widget.passwordController,
            obscureText: true,
            keyboardType: TextInputType.emailAddress,
            style: const TextStyle(color: Colors.white),
            decoration: InputDecoration(
                border: InputBorder.none,
                contentPadding: const EdgeInsets.only(top: 14),
                prefixIcon: const Icon(
                  Icons.lock,
                  color: Colors.white,
                ),
                hintText: widget.name,
                hintStyle: GoogleFonts.inter(
                  fontSize: 14,
                  color: Colors.white54,
                ),
            ),
          ),
        ),
      ],
    );
  }
}

class ForgotPassword extends StatelessWidget {
  const ForgotPassword({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      alignment: Alignment.centerRight,
      child: TextButton(
        onPressed: () => print("Pressed"),
        child: const Text(
          "Forgot Password",
          style: TextStyle(
              color: Colors.white,
              fontFamily: "OpenSans",
              decoration: TextDecoration.underline),
        ),
      ),
    );
  }
}

class LoginButton extends StatelessWidget {
  const LoginButton({super.key});
  @override
  Widget build(BuildContext context) {
    return Container(
      alignment: Alignment.center,
      padding: const EdgeInsets.symmetric(vertical: 10),
      width: double.infinity,
      child: ElevatedButton(
          onPressed: () {
            if (true) {
              Route route =
                  MaterialPageRoute(builder: (context) => const HomePage());
              Navigator.pushReplacement(context, route);
            }
          },
          style: ElevatedButton.styleFrom(
            padding: const EdgeInsets.all(12.5),
            minimumSize: const Size(400, 50),
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(15.0),
            ),
            backgroundColor: Colors.white,
          ),
          child: const Text(
            "LOGIN",
            style: TextStyle(
              color: Colors.black87,
              fontFamily: "OpenSans",
              fontSize: 20.0,
              fontWeight: FontWeight.bold,
            ),
          )
      ),
    );
  }
}

class ExitProfileButton extends StatelessWidget {
  const ExitProfileButton({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      alignment: Alignment.topLeft,
      padding: const EdgeInsets.symmetric(vertical: 10),
      width: double.infinity,
      child: IconButton(
        icon: const Icon(
          color: Colors.black,
          Icons.arrow_back,
        ),
        onPressed: () => Navigator.pop(context),
        style: ElevatedButton.styleFrom(
          // padding: const EdgeInsets.all(12.5),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(15.0),
          ),
          backgroundColor: Colors.black,
        ),
      ),
    );
  }
}

class BackToHomeButton extends StatelessWidget {
  const BackToHomeButton({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      alignment: Alignment.topLeft,
      padding: const EdgeInsets.symmetric(vertical: 10),
      width: double.infinity,
      child: IconButton(
        alignment: Alignment.topLeft,
        icon: const Icon(
          Icons.arrow_back,
          color: Colors.white,
        ),
        onPressed: () => Navigator.pop(context),
        style: ElevatedButton.styleFrom(
          // padding: const EdgeInsets.all(12.5),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(15.0),
          ),
          backgroundColor: Colors.white,
        ),
      ),
    );
  }
}

class ErrorMessage extends StatefulWidget {
  const ErrorMessage({Key? key}) : super(key: key);

  @override
  State<ErrorMessage> createState() => _ErrorMessageState();
}

class _ErrorMessageState extends State<ErrorMessage> {
  @override
  Widget build(BuildContext context) {
    return Container();
  }
}

class SecurCodeInput extends StatefulWidget {
  final usernameController = TextEditingController();
  SecurCodeInput({Key? key}) : super(key: key);

  @override
  State<SecurCodeInput> createState() => _SecurCodeInputState();
}

class _SecurCodeInputState extends State<SecurCodeInput> {
  final textUtils = TextUtils();
  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        textUtils.buildText(
            "Secure Code",
            14,
            Colors.white,
            FontWeight.bold),
        const SizedBox(height: 10.0),
        Container(
          alignment: Alignment.centerLeft,
          decoration: BoxDecoration(
            color: const Color.fromARGB(120, 175, 180, 255),
            borderRadius: BorderRadius.circular(10),
          ),
          height: 60,
          child: TextField(
            maxLength: 6,
            controller: widget.usernameController,
            keyboardType: TextInputType.name,
            style: const TextStyle(color: Colors.white),
            decoration: InputDecoration(
                border: InputBorder.none,
                contentPadding: const EdgeInsets.only(top: 14),
                prefixIcon: const Icon(
                  Icons.email,
                  color: Colors.white,
                ),
                hintText: "Enter the temporary code that we sent",
                hintStyle: GoogleFonts.inter(
                    fontSize: 14,
                    color: Colors.white54,
                ),
            ),
          ),
        ),
      ],
    );
  }
}
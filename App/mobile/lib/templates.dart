import 'package:flutter/material.dart';
import 'package:artopia/home_page.dart';
import 'package:artopia/login_page.dart';

class UsernameInput extends StatefulWidget {
  final usernameController = TextEditingController();

  UsernameInput({Key? key}) : super(key: key);

  @override
  State<UsernameInput> createState() => _UsernameInputState();
}

class _UsernameInputState extends State<UsernameInput> {
  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        const Text("Username",
            style: TextStyle(
              color: Colors.white,
              fontFamily: "OpenSans",
              fontWeight: FontWeight.bold,
            )),
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
            style: TextStyle(color: Colors.white),
            decoration: InputDecoration(
                border: InputBorder.none,
                contentPadding: EdgeInsets.only(top: 14),
                prefixIcon: Icon(
                  Icons.email,
                  color: Colors.white,
                ),
                hintText: "Enter your username",
                hintStyle: TextStyle(
                  color: Colors.white54,
                  fontFamily: 'OpenSans',
                )),
          ),
        ),
      ],
    );
  }
}

class EmailInput extends StatefulWidget {
  final emailController = TextEditingController();

  EmailInput({super.key});

  @override
  State<EmailInput> createState() => _EmailInputState();
}

class _EmailInputState extends State<EmailInput> {
  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        const Text("Email",
            style: TextStyle(
              color: Colors.white,
              fontFamily: "OpenSans",
              fontWeight: FontWeight.bold,
            )),
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
            style: TextStyle(color: Colors.white),
            decoration: InputDecoration(
                border: InputBorder.none,
                contentPadding: EdgeInsets.only(top: 14),
                prefixIcon: Icon(
                  Icons.email,
                  color: Colors.white,
                ),
                hintText: "Enter your email",
                hintStyle: TextStyle(
                  color: Colors.white54,
                  fontFamily: 'OpenSans',
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
  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        Text(widget.name,
            style: const TextStyle(
              color: Colors.white,
              fontFamily: "OpenSans",
              fontWeight: FontWeight.bold,
            )),
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
                hintStyle: const TextStyle(
                  color: Colors.white54,
                  fontFamily: 'OpenSans',
                )),
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
          )),
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

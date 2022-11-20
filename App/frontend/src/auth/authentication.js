import React from "react";
import { createContext, useContext, useState, useMemo } from "react";
//import { useHistory } from "react-router-dom";
import { Navigate } from "react-router-dom";

const UserContext = createContext();

export const useAuth = () => {
  return useContext(UserContext);
};

export const AuthProvider = ({ children }) => {
  const [token, setToken] = useState(() =>
    window.localStorage.getItem("token")
      ? JSON.parse(window.localStorage.getItem("token"))
      : null
  );

  //const history = useHistory();

  //log in
  const saveToken = (token) => {
    setToken(token);
    window.localStorage.setItem(
      "token",   //key
      JSON.stringify(token)  //value
    );
    //history.push("/");
  };

  //log out
  const clearToken = () => {
    setToken(null);
    window.localStorage.removeItem("token");
    //history.push("/");
  };

  const contextData = useMemo(
    () => ({
      token,
      saveToken,
      clearToken,
    }),
    [token]
  );

  return (
    <UserContext.Provider value={contextData}>{children}</UserContext.Provider>
  );
};

export const AuthenticatedRoute = ({ children }) => {
  const { token } = useAuth();
  if (!token) {
    return <Navigate to="/"/>;
  }
  return children;
};
import MainNavigation from "./MainNavigation";
import "./styles/Layout.css";

function Layout(props) {
  return (
    <div>
      <MainNavigation />
      <main className="layout-main">{props.children}</main>
    </div>
  );
}

export default Layout;

import React from "react";
import { useForm } from "react-hook-form";
import { Redirect, useHistory, useLocation } from "react-router-dom";
import { loginRoute } from "../../../AppRoutes";
import Button from "../../../components/Button";
import TextField from "../../../components/TextField";
import { AuthContext, useAppContext } from "../AuthProvider";

export default function PasswordForm() {
  const authContext = useAppContext(AuthContext);
  const authLoading = authContext.loading;

  const { handleSubmit, register } = useForm<{ password: string }>();
  const history = useHistory();
  const location = useLocation<{ username: string }>();

  const onSubmit = handleSubmit(async (data: { password: string }) => {
    authContext.passwordLogin({
      username: location.state.username,
      password: data.password,
    });
  });

  const backClicked = () => {
    authContext.clearError();
    history.push(loginRoute, location.state);
  };

  return (
    <>
      {!location.state.username && <Redirect to={loginRoute} />}
      <form onSubmit={onSubmit}>
        <TextField
          label="Username/email"
          value={location.state.username}
          disabled
        ></TextField>
        <TextField
          label="Password"
          name="password"
          inputRef={register({ required: true })}
          type="password"
        ></TextField>
        <Button onClick={backClicked}>Back</Button>
        <Button onClick={onSubmit} loading={authLoading} type="submit">
          Log in
        </Button>
      </form>
    </>
  );
}

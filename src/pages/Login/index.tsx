import { useMutation } from '@tanstack/react-query';
import { login } from '../../services/auth';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

import Button from "../../components/Button";
import Input from "../../components/Input";
import styles from './styles.module.css';

interface TimeResponse {
  time: string;
}

interface Form {
  username: string;
  password: string;
}

function Login() {
  const navigate = useNavigate();
  const [form, setForm] = useState<Form>({ username: "", password: "" });

  const { mutate, error, isPending } = useMutation<TimeResponse, Error, Form>({
    mutationFn: login,
  });

  const handleLogin = (form: Form) => {
    mutate(form, {
      onSuccess: () => {
        console.log("Arroz");
        navigate('/');
      },
      onError: (error) => {
        console.error('Erro ao logar:', error);
      }
    });
  };

  return (
    <div
      className={styles.background}
      style={{ backgroundImage: "url('/bg.jpg')" }}
    >
      <section className={styles.card}>
        <h1 className={styles.title}>Login</h1>

        <div className={styles.fieldGroup}>
          <label className={styles.label}>
            <span>Username</span>
            <Input
              className={styles.input}
              value={form.username}
              type="text"
              onChange={(e) => setForm({ ...form, username: e.target.value })}
            />
          </label>

          <label className={styles.label}>
            <span>Password</span>
            <Input
              className={styles.input}
              value={form.password}
              type="password"
              onChange={(e) => setForm({ ...form, password: e.target.value })}
            />
          </label>
        </div>

        <Button className={styles.button} onClick={() => handleLogin(form)}>
          Logar
        </Button>

        {isPending && <p className={styles.pending}>Carregando...</p>}
        {error && <p className={styles.error}>Erro: {error?.message}</p>}
      </section>
    </div>
  );
}

export default Login;

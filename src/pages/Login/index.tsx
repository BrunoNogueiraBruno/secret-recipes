import { useMutation } from '@tanstack/react-query'
import { login } from '../../services/auth';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom'

interface TimeResponse {
  time: string;
}

interface Form {
  username: string;
  password: string;
}

function Login() {
  const navigate = useNavigate()
  const [form, setForm] = useState<Form>({ username: "", password: "" });

  const { mutate, error, isPending } = useMutation<TimeResponse, Error, Form>({
    mutationFn: login,
  });

  const handleLogin = (form: Form) => {
  mutate(form, {
    onSuccess: () => {
        console.log("Arroz")
      navigate('/');
    },
    onError: (error) => {
      console.error('Erro ao logar:', error);
    }
  });
}

  if (isPending) return <p>Carregando...</p>
  if (error) return <p>Erro: {error.message}</p>

  return (
    <div>
      <label>
        Username
        <input
          value={form.username}
          type="text"
          onChange={(e) => setForm({ ...form, username: e.target.value })}
        />
      </label>
      <label>
        Password
        <input
          value={form.password}
          type="password"
          onChange={(e) => setForm({ ...form, password: e.target.value })}
        />
      </label>
      <button onClick={() => handleLogin(form)}>Logar</button>
    </div>
  );
}

export default Login;

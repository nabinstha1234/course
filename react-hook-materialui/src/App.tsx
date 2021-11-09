import {
  useForm,
  SubmitHandler,
  FormProvider,
} from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as yup from 'yup';
import './App.css';
import Form from './Component/Form';
import Form1 from './Component/Form1';
import App1 from './pages/App1';

interface IFormInputs {
  email: string;
  password: string;
  firstName: string;
  lastName: string;
}

const schema = yup.object().shape({
  email: yup.string().email().required(),
  password: yup.string().max(32).min(8).required(),
  firstName: yup.string().required(),
  lastName: yup.string().required(),
});

function App() {
  const methods = useForm<IFormInputs>({
    resolver: yupResolver(schema),
  });

  const formSubmitHandler: SubmitHandler<IFormInputs> = (
    data: IFormInputs,
  ) => {
    console.log('data', data);
  };
  console.log('form data is ', methods.watch('email'));

  return (
    <div className="App">
      <FormProvider {...methods}>
        <form onSubmit={methods.handleSubmit(formSubmitHandler)}>
          <Form />
          <br />
          <Form1 />
          {/* <br /> */}
          {/* <input
          defaultValue="example@leo.com"
          {...register('email')}
        />
        <br />
        <input {...register('password')} />
        <br />
        {errors.password && errors.password.message && (
          <span>{errors.password.message}</span>
        )}
        <br />
        */}
          <br />
          <input type="submit" />
        </form>
      </FormProvider>
      {/* Form Part 2 */}
      <h1>Form Part two</h1>
      <App1 />
    </div>
  );
}

export default App;

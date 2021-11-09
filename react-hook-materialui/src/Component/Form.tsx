import { TextField } from '@material-ui/core';
import { Controller, useFormContext } from 'react-hook-form';

function Form() {
  const {
    control,
    formState: { errors },
  } = useFormContext();

  return (
    <div>
      <Controller
        name="email"
        control={control}
        defaultValue="shresthanabin94@gmail.com"
        render={({ field }) => (
          <TextField
            {...field}
            label="Email"
            type="email"
            variant="outlined"
            error={!!errors.email}
            helperText={errors.email ? errors.email.message : ''}
          ></TextField>
        )}
      />
      <br />
      <br />
      <Controller
        name="password"
        control={control}
        defaultValue=""
        render={({ field }) => (
          <TextField
            {...field}
            label="Password"
            type="password"
            variant="outlined"
            error={!!errors.email}
            helperText={errors.email ? errors.email.message : ''}
          ></TextField>
        )}
      />
    </div>
  );
}

export default Form;

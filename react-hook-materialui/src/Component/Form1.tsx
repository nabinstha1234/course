import { TextField } from '@material-ui/core';
import { Controller, useFormContext } from 'react-hook-form';

function Form1() {
  const {
    control,
    formState: { errors },
  } = useFormContext();
  return (
    <div>
      <Controller
        name="firstName"
        control={control}
        defaultValue="Nabin"
        render={({ field }) => (
          <TextField
            {...field}
            label="First Name"
            type="text"
            variant="outlined"
            error={!!errors.firstName}
            helperText={
              errors.firstName ? errors.lastName.message : ''
            }
          ></TextField>
        )}
      />
      <br />
      <br />
      <Controller
        name="lastName"
        control={control}
        defaultValue="Shrestha"
        render={({ field }) => (
          <TextField
            {...field}
            label="Last Name"
            type="text"
            variant="outlined"
            error={!!errors.lastName}
            helperText={
              errors.lastName ? errors.lastName.message : ''
            }
          ></TextField>
        )}
      />
    </div>
  );
}

export default Form1;

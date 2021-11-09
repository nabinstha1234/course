import { IIngredient } from './lingredient';
import { IInstruction } from './IInstruction';

export interface IRecipe {
  recipeId: string | undefined;
  title: string;
  description: string;
  instructions: Array<IInstruction>;
  ingredients: Array<IIngredient>;
}

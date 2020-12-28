import {NgModule} from '@angular/core'
import {Routes, RouterModule} from '@angular/router';

import { FrontendComponent } from './components/frontend/frontend.component';
import { BackendComponent } from './components/backend/backend.component';
import { PageNotFoundComponent } from './components/page-not-found/page-not-found.component';

const routes: Routes = [
  // {path: '', redirectTo: '/frontend', pathMatch: 'full'},
  {path: '', component: FrontendComponent},
  {path: 'backend', component: BackendComponent},
  {path: '**', component: PageNotFoundComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
export const routingModule = [
  FrontendComponent,
  BackendComponent,
  PageNotFoundComponent,
]

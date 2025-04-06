import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BackgroundcomponentComponent } from './backgroundcomponent.component';

describe('BackgroundcomponentComponent', () => {
  let component: BackgroundcomponentComponent;
  let fixture: ComponentFixture<BackgroundcomponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BackgroundcomponentComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(BackgroundcomponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

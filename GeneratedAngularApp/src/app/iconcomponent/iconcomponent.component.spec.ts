import { ComponentFixture, TestBed } from '@angular/core/testing';

import { IconcomponentComponent } from './iconcomponent.component';

describe('IconcomponentComponent', () => {
  let component: IconcomponentComponent;
  let fixture: ComponentFixture<IconcomponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [IconcomponentComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(IconcomponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

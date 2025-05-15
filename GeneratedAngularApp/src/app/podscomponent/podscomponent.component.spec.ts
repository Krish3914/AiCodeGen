import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PodscomponentComponent } from './podscomponent.component';

describe('PodscomponentComponent', () => {
  let component: PodscomponentComponent;
  let fixture: ComponentFixture<PodscomponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PodscomponentComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(PodscomponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

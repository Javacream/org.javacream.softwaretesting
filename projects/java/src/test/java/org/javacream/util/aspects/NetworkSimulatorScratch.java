package org.javacream.util.aspects;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.reflect.MethodSignature;
import org.springframework.context.annotation.Profile;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

import java.util.Collection;

@Component
@Aspect
@Profile("aop")
@Order(10)
public class NetworkSimulatorAspect{

    @Around("execution(* org.javacream..impl.*Service.*(..))")
    public Object trace(ProceedingJoinPoint pjp) throws Throwable {
        Thread.sleep(10);
        Object result = pjp.proceed(SerializationUtils.clone(pjp.getArgs()));
        return SerializationUtils.clone(result)
    }
}
